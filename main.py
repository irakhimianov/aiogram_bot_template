import asyncio
import logging
from loader import dp, bot
from utils import on_startup_notify, set_default_commands
from middlewares import *


async def on_startup():
    logging.basicConfig(
        format=u'%(filename)s:%(lineno)-d #%(levelname)-16s [%(asctime)s] %(message)s',
        level=logging.INFO
    )
    # middlewares
    logging.info('Setting up middlewares...')
    #dp.setup_middleware(#MiddleWareName)

    logging.info('Everything is ready to launch!')
    # Set default commands (/start and /help)
    await set_default_commands(dp)

    # Notify admin that the bot has started
    await on_startup_notify(dp)
    await dp.skip_updates()
    await dp.start_polling()


async def on_shutdown():
    logging.info('Shutting down...')
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
