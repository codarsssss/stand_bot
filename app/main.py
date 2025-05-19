from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)
from .config import BOT_TOKEN, DEBUG
from .db import init_db
from .handlers import start, handle_name, toggle_standing, health, debug
from .errors import error_handler


def main():
    init_db()
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))
    app.add_handler(CallbackQueryHandler(toggle_standing))
    app.add_handler(CommandHandler("health", health))

    if DEBUG:
        app.add_handler(CommandHandler("debug", debug))

    app.add_error_handler(error_handler)
    app.run_polling()


if __name__ == "__main__":
    main()
