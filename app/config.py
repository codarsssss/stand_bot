import os
import logging
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

LANG = os.getenv("LANG", "ru")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
)
logger = logging.getLogger(__name__)
