from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMINS


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in ADMINS
