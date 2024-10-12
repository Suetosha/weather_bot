from aiogram import Router
from aiogram.types import Message

from lexicon import lexicon
from services.get_weather import Weather

router = Router()


@router.message()
async def get_weather_by_city_command(message: Message):
    city = message.text
    weather = Weather(city)
    try:
        text = weather.format_weather_text()
        await message.answer(text, parse_mode='HTML')
    except:
        await message.answer(lexicon.CITY_NOT_FOUND)
