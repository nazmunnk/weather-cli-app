import requests

while True:
    city_name = input("Write a name of City: ")

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city_name, "count": 1}
    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()
    if "results" not in geo_data:
        print("Not found! Write a correct name")
    else:
        break

city = geo_data["results"][0]
lat = city["latitude"]
lon = city["longitude"]


weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()
weather = weather_data["current_weather"]

weather_descriptions = {
    0: "Clear sky ☀️",
    1: "Mainly clear 🌤️",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️",
    61: "Light rain 🌧️",
    63: "Moderate rain 🌧️",
    65: "Heavy rain 🌧️",
    80: "Rain showers 🌦️",
    }
code = weather["weathercode"]
description = weather_descriptions.get(code, "অজানা আবহাওয়া")

    
print("─────────────────────────────")
print(f"  City        : {city_name}")
print(f"  Temperature : {weather['temperature']} °C")
print(f"  Wind speed  : {weather['windspeed']} km/h")
print(f"  Weather     : {description}")

