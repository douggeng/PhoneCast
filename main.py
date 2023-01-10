import schedule
import requests
import time
from secret_api_key import noti_api_key, weather_api_key

def main():
    #schdule the push notification by changing time 
    schedule.every().day.at("08:00").do(weather)
    schedule.every().day.at("17:00").do(weather)

    while True:
        schedule.run_pending()
        time.sleep(1)

def weather():
    #Grabbing API_website, API_key, and City location
    URL_API = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = weather_api_key
    CITY = "Gilbert"

    #Making URL and getting the API request response
    URL = URL_API + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(URL).json()

    #placeholders for kelvin & meter/s
    temp_kelvin = response['main']['temp']
    temp_meters = response['wind']['speed']

    #Variables for weather information
    fahrenheit = calculate_fahrenheit(temp_kelvin)
    wind_speed = calculate_mph(temp_meters)
    skies = response['weather'][0]['description']
    humidity = response['main']['humidity']

    #Sends push notification
    requests.post('https://api.mynotifier.app', {
        "apiKey": noti_api_key,
        "message": "Weather Report!",
        "description": (f"Temperature in {CITY}: {fahrenheit:.0f}°F, {skies}, Wind: {wind_speed:.0f} mph, Humidity: {humidity}%")
        })

#Converting kevlin to Fahrenheit
def calculate_fahrenheit(kelvin):
    fahrenheit = round(kelvin - 273.15)*(9/5) +32
    return fahrenheit

#Converting meter/s to Mph
def calculate_mph(meters):
    mph = round(meters * 2.237)
    return mph


if __name__ == "__main__":
    main()