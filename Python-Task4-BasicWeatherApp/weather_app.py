
import requests
print("===== BASIC WEATHER APP =====")

def weather_description(code):
    if code == 0:
        return "Clear Sky"
    elif code in [1, 2, 3]:
        return "Partly Cloudy or Cloudy"
    elif code in [45, 48]:
        return "Foggy"
    elif code in [51, 53, 55, 56, 57]:
        return "Drizzle"
    elif code in [61, 63, 65, 66, 67, 80, 81, 82]:
        return "Rainy"
    elif code in [71, 73, 75, 77, 85, 86]:
        return "Snowy"
    elif code in [95, 96, 99]:
        return "Thunderstorm"
    else:
        return "Unknown"


while True:
    city = input("\nEnter city name: ").strip()

    if not city:
        print("Error: Please enter a city name.")
        continue

    try:
        # Find the city's coordinates
        location_url = "https://geocoding-api.open-meteo.com/v1/search"

        location_response = requests.get(
            location_url,
            params={"name": city, "count": 1},
            timeout=10
        )
        location_response.raise_for_status()
        location_data = location_response.json()

        if not location_data.get("results"):
            print("Error: City not found. Try again.")
            continue

        location = location_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]

        # Get current weather information
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "weather_code,"
                    "wind_speed_10m"
                )
            },
            timeout=10
        )
        weather_response.raise_for_status()

        data = weather_response.json()
        current = data["current"]

        temp_c = current["temperature_2m"]
        temp_f = (temp_c * 9 / 5) + 32
        humidity = current["relative_humidity_2m"]
        wind = current["wind_speed_10m"]
        condition = weather_description(current["weather_code"])

        print("\n===== CURRENT WEATHER =====")
        print("City:", location["name"])
        print(f"Temperature: {temp_c:.1f} °C")
        print(f"Temperature: {temp_f:.1f} °F")
        print(f"Humidity: {humidity}%")
        print("Weather Condition:", condition)
        print(f"Wind Speed: {wind} km/h")
        print("===========================")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print("Error: Unable to fetch weather. Check your internet.")

    except (KeyError, ValueError, TypeError):
        print("Error: Unexpected weather data received.")

    again = input("\nCheck another city? (yes/no): ").strip().lower()

    if again not in ("yes", "y"):
        print("\nThank you for using Weather App!")
        break
