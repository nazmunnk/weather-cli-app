#import requests

#response = requests.get("https://jsonplaceholder.typicode.com/users/1")
#print(response.status_code)
#print(response.text)



#x = requests.get('https://w3schools.com/python/demopage.htm')

#print(x.text)
"""
import requests
from requests.exceptions import HTTPError

URLS = ["https://api.github.com", "https://api.github.com/invalid"]

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")

import requests
response = requests.get("https://api.github.com")

print(response.content)
print(type(response.content))

import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 23.81,
    "longitude": 90.41,
    "current_weather": True
}

response = requests.get(url, params=params)
#print(response.status_code)
#print(response.json())



data = response.json()

weather = data["current_weather"]
print("তাপমাত্রা:", weather["temperature"], "°C")
print("বাতাসের গতি:", weather["windspeed"], "km/h")
import requests

# ইউজারের কাছ থেকে শহরের নাম নেওয়া
city_name = input("শহরের নাম লিখুন (ইংরেজিতে): ")

# ধাপ ১: শহরের নাম দিয়ে lat/long বের করা
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city_name, "count": 1}
geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

# শহর খুঁজে পাওয়া না গেলে বন্ধ করা
if "results" not in geo_data:
    print("শহরটি খুঁজে পাওয়া যায়নি! সঠিক নাম লিখুন।")
else:
    city = geo_data["results"][0]
    lat = city["latitude"]
    lon = city["longitude"]

    # ধাপ ২: সেই lat/long দিয়ে আবহাওয়ার data আনা
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()

    weather = weather_data["current_weather"]

    # ধাপ ৩: সুন্দর করে প্রিন্ট করা
    print("─────────────────────────────")
    print(f"  শহর       : {city_name}")
    print(f"  তাপমাত্রা : {weather['temperature']} °C")
    print(f"  বাতাসের গতি: {weather['windspeed']} km/h")
    print("─────────────────────────────")
    """
import requests

city_name = input("শহরের নাম লিখুন: ")

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city_name, "count": 1}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()
geo_list=geo_data["results"][0]
print(geo_list["name"], geo_list["id"])

"""
name_list=["xyz","abc","dce","ctg"]
while True:
    name=input("enter a name: ")
    if name in name_list:
        break
    else:
       print("successful!")
# ইউজারের কাছ থেকে শহরের নাম নেওয়া
city_name = input("শহরের নাম লিখুন (ইংরেজিতে): ")

# ধাপ ১: শহরের নাম দিয়ে lat/long বের করা
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city_name, "count": 1}
geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

# শহর খুঁজে পাওয়া না গেলে বন্ধ করা
if "results" not in geo_data:
    print("শহরটি খুঁজে পাওয়া যায়নি! সঠিক নাম লিখুন।")

else:
    city = geo_data["results"][0]
    lat = city["latitude"]
    lon = city["longitude"]

    # ধাপ ২: সেই lat/long দিয়ে আবহাওয়ার data আনা
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
        0: "পরিষ্কার আকাশ ☀️",
        1: "প্রায় পরিষ্কার 🌤️",
        2: "আংশিক মেঘলা ⛅",
        3: "মেঘাচ্ছন্ন ☁️",
        61: "হালকা বৃষ্টি 🌧️",
        63: "মাঝারি বৃষ্টি 🌧️",
        65: "ভারী বৃষ্টি 🌧️",
        80: "ঝরঝরে বৃষ্টি 🌦️",
    }
    code = weather["weathercode"]
    description = weather_descriptions.get(code, "অজানা আবহাওয়া")

    # ধাপ ৩: সুন্দর করে প্রিন্ট করা
    print("─────────────────────────────")
    print(f"  শহর       : {city_name}")
    print(f"  তাপমাত্রা : {weather['temperature']} °C")
    print(f"  বাতাসের গতি: {weather['windspeed']} km/h")
    print(f"  আবহাওয়া   : {description}")
    print("─────────────────────────────")
"""