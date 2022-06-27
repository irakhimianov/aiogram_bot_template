from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    # Command '/start' handler
    await bot.send_message(text='Template start message'
                           chat_id=message.from_user.id)