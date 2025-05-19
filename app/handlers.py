from telegram import Update
from telegram.ext import ContextTypes

from .db import get_user, add_user, update_standing
from .keyboard import get_main_button
from .config import GROUP_CHAT_ID, ADMIN_CHAT_ID, LANG
from .messages import MESSAGES


def is_admin(user_id):
    return str(user_id) == str(ADMIN_CHAT_ID)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    if user is None:
        await update.message.reply_text(MESSAGES[LANG]["enter_name"])
    else:
        await send_main_button(update, context)


async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if get_user(user_id) is None:
        name = update.message.text.strip()
        add_user(user_id, name)
        await send_main_button(update, context)


async def send_main_button(update_or_query, context: ContextTypes.DEFAULT_TYPE):
    user_id = update_or_query.effective_user.id
    user = get_user(user_id)
    if user is None:
        return

    _, standing = user
    markup = get_main_button(standing)

    text = MESSAGES[LANG]["go_to_group"]

    if isinstance(update_or_query, Update) and update_or_query.message:
        await update_or_query.message.reply_text(
            text, reply_markup=markup, parse_mode="Markdown"
        )
    elif update_or_query.callback_query:
        await update_or_query.callback_query.edit_message_text(
            text, reply_markup=markup, parse_mode="Markdown"
        )


async def toggle_standing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    user = get_user(user_id)
    if user is None:
        await query.message.reply_text(MESSAGES[LANG]["not_registered"])
        return

    name, standing = user
    new_standing = not bool(standing)
    update_standing(user_id, new_standing)

    status_text = (
        MESSAGES[LANG]["standing"].format(name=name)
        if new_standing
        else MESSAGES[LANG]["not_standing"].format(name=name)
    )

    await context.bot.send_message(chat_id=GROUP_CHAT_ID, text=status_text)
    await send_main_button(update, context)


async def health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    await update.message.reply_text(MESSAGES[LANG]["health_ok"])


async def debug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    chat = update.effective_chat
    await update.message.reply_text(
        f"Chat ID: {chat.id}\n"
        f"Chat Title: {chat.title or '-'}\n"
        f"Username: @{update.effective_user.username or '-'}"
    )
