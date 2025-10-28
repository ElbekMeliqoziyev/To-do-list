from aiogram import Bot, Dispatcher
from environs import Env

from handler import start_r

import asyncio, logging

dp = Dispatcher()

env = Env()
env.read_env()

async def main():
    bot = Bot(env.str("TOKEN"))
    dp.include_router(start_r)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Bot ishda")
    asyncio.run(main())