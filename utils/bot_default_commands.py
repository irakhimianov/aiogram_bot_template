from aiogram import types
from aiogram import Dispatcher


async def set_default_commands(dp: Dispatcher) -> None:
    # Pop-up tips when '/' is typed in chat-window with bot
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Start bot'),
            types.BotCommand('help', 'What this bot can do'),
        ]
    )
