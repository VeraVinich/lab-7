import requests

def weather():
    def get_weather(city_name, api_key):
        OWM_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru"
        
        try:
            response = requests.get(OWM_URL)
            response.raise_for_status()
            data = response.json()
        
            return {
                "Температура": f"{data['main']['temp']}°C",
                "Влажность": f"{data['main']['humidity']}%",
                "Давление": f"{data['main']['pressure']} hPa",
            }
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
            return None
        
    city = "Saint Petersburg"
    OWM_API_KEY = "71d3d3bfe464980c34604066d9cb27ed"

    weather_info = get_weather(city, OWM_API_KEY)

    if weather_info:
        print(f"Погода в городе {city}:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
    print()


if __name__ == "__main__":
    weather()