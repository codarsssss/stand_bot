import traceback

from .config import ADMIN_CHAT_ID, logger


async def error_handler(update, context):
    error_text = "".join(traceback.format_exception(
        None, context.error, context.error.__traceback__
    ))
    message = f"⚠️ Произошла ошибка:\n<pre>{error_text}</pre>"

    logger.error("Ошибка: %s", error_text)

    if ADMIN_CHAT_ID:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID, text=message, parse_mode="HTML"
        )
