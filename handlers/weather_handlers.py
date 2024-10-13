from aiogram import Router
from aiogram.types import Message

from services.get_weather import Weather
from validators.date_validator import date_validator
from validators.params_validator import params_validator

router = Router()


@router.message()
async def get_weather_by_city_command(message: Message):
    try:
        params = message.text.split(' ')
        params_validator(params=params)
        city, date = params
        date = date_validator(user_date=date, current_date=message.date)
        weather = Weather(city, date)
        weather_by_date = weather.get_weather_info()
        text = weather.format_weather_text(*weather_by_date)
        await message.answer(text, parse_mode='HTML')

    except Exception as e:
        await message.answer(e.__str__())
