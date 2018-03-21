# fetching weather data using openweathermap api
# need to sign up for free api key at openweathermap.org

import requests
import json

API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "C")
        print("Feels like:", data["main"]["feels_like"], "C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind speed:", data["wind"]["speed"], "m/s")
    else:
        print("Error:", response.status_code)
        print(response.text)

# test it
get_weather("Kathmandu")
get_weather("New York")
get_weather("London")
# weather
# fix key
# weather
