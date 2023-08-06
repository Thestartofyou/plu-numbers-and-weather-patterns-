import requests

def get_weather_data(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def plu_number_correlation(weather_data):
    # Replace this with your correlation logic
    # For this example, let's assume the correlation is based on temperature
    temperature = weather_data["main"]["temp"]
    if temperature >= 25:
        return "PLU: 1234"
    elif temperature >= 15:
        return "PLU: 5678"
    else:
        return "PLU: 9101"

def main():
    api_key = "YOUR_API_KEY"  # Replace this with your actual API key
    city_name = "New York"    # Replace this with the desired city name

    try:
        weather_data = get_weather_data(api_key, city_name)
        plu_number = plu_number_correlation(weather_data)
        print(f"Weather data for {city_name}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print("Correlated PLU Number:", plu_number)
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
    except KeyError as e:
        print("Invalid response format from API:", e)

if __name__ == "__main__":
    main()

