import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return None

    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    city = input("Enter a city name: ")

    try:
        coords = get_coordinates(city)
        if coords is None:
            print("Error: City not found.")
            return

        lat, lon, name = coords
        weather_data = get_weather(lat, lon)

        if "current_weather" not in weather_data:
            print("Error: Could not fetch weather data.")
            return

        current = weather_data["current_weather"]
        print(f"\nWeather in {name}:")
        print(f"Temperature: {current['temperature']}°C")
        print(f"Wind Speed: {current['windspeed']} km/h")

    except requests.exceptions.RequestException:
        print("Error: Failed to connect to the API.")

if __name__ == "__main__":
    main()