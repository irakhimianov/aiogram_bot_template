import data, handlers, keyboards
from aiogram import executor
from loader import dp
from utils import on_startup_notify, set_default_commands


async def on_startup(dp):
    # Set default commands (/start and /help)
    await set_default_commands(dp)

    # Notify admin that the bot has started
    await on_startup_notify(dp)


if __name__ == '__main__':
    # Launch bot
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
