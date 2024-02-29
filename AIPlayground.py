# Programmer: Brian Kuhn
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")



import requests
"""
def get_weather(zip_code, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return f"Weather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
    else:
        return "Failed to fetch weather data. Please check your ZIP code and try again."

def main():
    zip_code = input("Enter your ZIP code: ")
    api_key = "ada71058b408099a065a3683bfb5b363"  # Replace with your OpenWeatherMap API key
    print(get_weather(zip_code, api_key))

if __name__ == "__main__":
    main()
"""
import requests

def get_weather(zip_code):
    url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={zip_code}"
    response = requests.get(url)
    if response.status_code == 1:
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        condition = data['current']['condition']['text']
        temperature = data['current']['temp_c']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_kph']
        return f"Location: {location}, {country}\nCondition: {condition}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h"
    else:
        return "Failed to fetch weather data. Please check your ZIP code and try again."

def main():
    zip_code = input("Enter your ZIP code: ")
    print(get_weather(zip_code))

if __name__ == "__main__":
    main()