import asyncio
import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import handlers
from loader import dp, bot, config
from services import notify_admin, set_default_commands

logger = logging.getLogger(__name__)


async def on_startup():
    logger.info('Setting up middlewares...')
    dp.setup_middleware(LoggingMiddleware())

    logger.info('Setting default commands...')
    await set_default_commands(dp)

    await notify_admin(dp, config.bot.admin)
    await dp.skip_updates()
    await dp.start_polling()


async def on_shutdown():
    logger.info('Shutting down...')
    await dp.storage.close()
    await dp.storage.wait_closed()
    bot_session = await bot.get_session()
    await bot_session.close()


async def main():
    try:
        await on_startup()
    finally:
        await on_shutdown()


if __name__ == '__main__':
    # Launch bot
    asyncio.get_event_loop().run_until_complete(main())
