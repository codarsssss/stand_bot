from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_main_button(standing: bool):
    button_text = "У меня не стоит ❌" if standing else "У меня стоит ✅"
    keyboard = [[InlineKeyboardButton(button_text, callback_data="toggle")]]
    return InlineKeyboardMarkup(keyboard)
