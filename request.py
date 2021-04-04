import os
import dotenv
import requests
import geocoder
import json

dotenv.load_dotenv()
Openweather_API_key = os.getenv("Openweather_API_key")

#Ipstack_API_key = os.getenv("Ipstack_API_key")

def respon():

    #location_response = requests.get(
    #    "http://api.ipstack.com/check?",
    #    params={
    #        "access_key": Ipstack_API_key,
    #        }
    #)
    #location = json.loads(location_response.text)
    #lat = location["latitude"]
    #lon = location["longitude"]

    weather_response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall?",
        params={
            "lat": geocoder.ip("me").lat,
            "lon": geocoder.ip("me").lng,
            "units": "metric",
            "APPID": Openweather_API_key,
            "exclude":"hourly,current,minutely,alerts",
            },
    )
    text = json.loads(weather_response.text)
    print(text)
    day_temps = {
    }

    today = text["daily"][1]
    day_temps.update(
            {
            "Morning":today["temp"]["morn"],
            "Day":today["temp"]["day"],
            "Evening":today["temp"]["eve"],
            "Night":today["temp"]["night"],
            "Max_temp":today["temp"]["max"],
            "min_temp":today["temp"]["min"],
            "realfeel": today["feels_like"]
            
        }
    )
    return day_temps
