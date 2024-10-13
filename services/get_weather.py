from datetime import datetime
from os import getenv

from dotenv import load_dotenv
import requests

load_dotenv()


class Weather:
    def __init__(self, city: str, date: datetime.date):
        self.city = city
        self.date = date

    def filter_by_day(self, weather_list: list) -> list:
        weather_filtered_list = list(
            filter(lambda i:
                   datetime.strptime(i['dt_txt'], '%Y-%m-%d %H:%M:%S').hour == 15 and
                   self.date.__str__() in i['dt_txt'], weather_list))

        return weather_filtered_list

    def get_weather_info(self):
        url = (f'http://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={getenv("API_KEY")}&'
               f'units=metric&'
               f'lang=ru&'
               )
        response = requests.get(url).json()
        if response.get('cod') != '200':
            raise Exception(response.get('message'))

        weather_info = response.get('list')
        weather_info = self.filter_by_day(weather_info)
        return weather_info

    def format_weather_text(self, weather):
        temp = round(weather['main']['temp'])
        temp_feels_like = round(weather['main']['feels_like'])
        max_temp = round(weather['main']['temp_max'])
        min_temp = round(weather['main']['temp_min'])
        description = weather['weather'][0]['description'].capitalize()

        text = (f'<b>{self.city}</b>\n'
                f'<b>{self.date}</b>\n'
                f'--------------------\n'
                f'{description}\n'
                f'На данный момент: {temp}°C\n'
                f'Ощущается как {temp_feels_like}°C\n'
                f'Максимум {max_temp}°C\n'
                f'Минимум {min_temp}°C')

        return text
