import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import main_handlers, weather_handlers

load_dotenv()

TOKEN = getenv("TOKEN")

dp = Dispatcher()

# Регистрация роутеров
dp.include_router(main_handlers.router)
dp.include_router(weather_handlers.router)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
