import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data import load_config, Config

logging.basicConfig(
    format=u'%(filename)s:%(lineno)-d #%(levelname)-16s [%(asctime)s] %(message)s',
    level=logging.INFO,
)

config: Config = load_config()
if config.redis.host and config.redis.port:
    storage = RedisStorage2(config.redis.host, config.redis.port, db=config.redis.db)
else:
    storage = MemoryStorage()
bot = Bot(token=config.bot.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)
