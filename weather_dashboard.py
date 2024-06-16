import requests
import matplotlib.pyplot as plt
import datetime

API_KEY = 'your_api_key_here'

def get_weather_data(city):
    """Fetch current weather data and forecast for a city from OpenWeatherMap API."""
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    forecast_url = 'http://api.openweathermap.org/data/2.5/forecast'
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    current_weather = response.json()
    
    response = requests.get(forecast_url, params=params)
    forecast = response.json()
    
    return current_weather, forecast

def plot_weather(forecast):
    """Plot the weather forecast data."""
    dates = [datetime.datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S') for item in forecast['list']]
    temps = [item['main']['temp'] for item in forecast['list']]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temperature (C)')
    plt.title('7-Day Weather Forecast')
    plt.grid(True)
    plt.show()

def display_weather(city):
    """Display current weather and forecast for a city."""
    current_weather, forecast = get_weather_data(city)
    
    if current_weather['cod'] == 200:
        print(f"City: {current_weather['name']}")
        print(f"Temperature: {current_weather['main']['temp']}°C")
        print(f"Weather: {current_weather['weather'][0]['description']}")
        print(f"Humidity: {current_weather['main']['humidity']}%")
        print(f"Pressure: {current_weather['main']['pressure']} hPa")
        
        plot_weather(forecast)
    else:
        print("City not found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather(city)
