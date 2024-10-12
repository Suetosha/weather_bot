from datetime import datetime
from os import getenv
from dotenv import load_dotenv
import time
import requests

load_dotenv()


class Weather:
    def __init__(self, city: str, date: datetime.date = None):
        self.city = city
        self.date = date

    def get_weather_info(self):
        url = (f'https://api.openweathermap.org/data/2.5/weather?'
               f'q={self.city}&'
               f'appid={getenv("API_KEY")}&'
               f'units=metric&'
               f'lang=ru&'
               )

        response = requests.get(url)
        weather_info = response.json()
        return weather_info

    def format_weather_text(self):
        weather_info = self.get_weather_info()

        temp = round(weather_info['main']['temp'])
        temp_feels_like = round(weather_info['main']['feels_like'])
        max_temp = round(weather_info['main']['temp_max'])
        min_temp = round(weather_info['main']['temp_min'])
        date_time = time.strftime('%d:%m:%Y, %H:%M', time.gmtime(weather_info['dt']))
        description = weather_info['weather'][0]['description'].capitalize()

        text = (f'<b>{self.city}:</b>\n'
                f'<b>{date_time}</b>\n'
                f'--------------------\n'
                f'{description}\n'
                f'На данный момент: {temp}°C\n'
                f'Ощущается как {temp_feels_like}°C\n'
                f'Максимум {max_temp}°C\n'
                f'Минимум {min_temp}°C')

        return text
