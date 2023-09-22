from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

city = "Tehran"


def get_current_weather(city="Tehran"):
    requests_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv('API_KEY')}&q={city}&units=imperial"

    weather_data = requests.get(requests_url).json()
    return weather_data


if __name__ == "__main__":
    print('\n*** ger weather condition***:')
    city = input('\n please enter a city name')

    if not bool(city.strip()):
        city = "Tehran"
    weather_data = get_current_weather(city)

    print('\n')
    pprint(weather_data)
