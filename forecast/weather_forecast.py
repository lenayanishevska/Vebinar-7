import requests
from decouple import config


def get_location() -> str:
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        city = data.get("city")
        if city:
            return city
        else:
            return "Location data not available."
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")


def get_forecast(location):
    url = "https://api.weatherapi.com/v1/current.json?"

    params = {
        "key": config('API_KEY'),
        "q": location
    }

    try:
        response = requests.get(url, params)
        data = response.json()

        if response.status_code == 200:
            print(f"Current temperature in {location} is {data['current']['temp_c']}")
            print(f"The temperature feels like {data['current']['feelslike_c']}")
            print(f"Humidity: {data['current']['humidity']}")
            print(f"Cloud: {data['current']['cloud']}")
            print(f"Wind speed (mph):{data['current']['wind_mph']}, wind direction: {data['current']['wind_dir']}")
            print(f"Pressure: {data['current']['pressure_mb']}")
            print(f"Weather condition: {data['current']['condition']['text']}")
        else:
            print(f"Error: {data['meta']['msg']}")

    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
