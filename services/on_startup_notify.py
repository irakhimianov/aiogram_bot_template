import logging

from aiogram import Dispatcher

logger = logging.getLogger(__name__)


async def notify_admin(dp: Dispatcher, admin_id: int) -> None:
    try:
        await dp.bot.send_message(admin_id, 'Бот запущен')
    except Exception as e:
        logger.error(e)
