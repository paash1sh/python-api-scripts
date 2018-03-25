# 5 day weather forecast
# uses the forecast endpoint instead of current weather

import requests

API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "cnt": 5  # number of forecasts (every 3 hours)
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print("5-day forecast for", city)
        print("-" * 40)
        for item in data["list"]:
            date = item["dt_txt"]
            temp = item["main"]["temp"]
            desc = item["weather"][0]["description"]
            print(f"{date} | {temp}C | {desc}")
    else:
        print("something went wrong:", response.status_code)

get_forecast("Kathmandu")
# forecast
# forecast
