import asyncio
from aiogram import Bot, Dispatcher
import logging

from handlers.handlers import router

import os
import dotenv


dotenv.load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
   

async def main():
  dp.include_router(router)
  await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="logs/zaboum_logs.txt", filemode="a")
    try:
       asyncio.run(main())
    except KeyboardInterrupt:
       print('Exit')