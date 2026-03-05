import os
import asyncio
import logging
from dotenv import load_dotenv
from telegram.ext import Application

from apps.bot import setup_bot
from apps.panel_bot import setup_panel

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN belum diset di Railway Variables")

async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    setup_bot(app)
    setup_panel(app)

    logger.info("🚀 IVASMS Premium Bot Running...")
    await app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
