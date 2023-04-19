import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Bot:
    token: str
    admin: int


@dataclass
class Redis:
    host: str
    port: int
    db: int


@dataclass
class Config:
    bot: Bot
    redis: Redis


def load_config() -> Config:
    load_dotenv()

    return Config(
        bot=Bot(
            token=os.getenv('TOKEN', ''),
            admin=int(os.getenv('ADMIN', '0'))
        ),
        redis=Redis(
            host=os.getenv('REDIS_HOST', ''),
            port=int(os.getenv('REDIS_PORT', '6379')),
            db=int(os.getenv('REDIS_DB', '5')),
        ),

    )
