# Basic Weather App

## OASIS InfoByte Internship – Task 4

**Domain:** Python Programming  
**Task:** Basic Weather App  
**Level:** Beginner

## Project Description

The Basic Weather App is a Python command-line application that retrieves and displays current weather information for a city entered by the user.

The application uses the free Open-Meteo API to fetch real-time weather data.

## Features

- Accepts a city name from the user.
- Retrieves weather information using an API.
- Displays temperature in Celsius (°C) and Fahrenheit (°F).
- Displays humidity percentage.
- Shows weather conditions such as clear, cloudy, rainy, and foggy.
- Displays wind speed in km/h.
- Handles invalid city names and empty inputs.
- Handles network errors and connection timeouts.
- Allows users to check the weather for multiple cities.

## Technologies Used

- Python 3
- Visual Studio Code
- Python `requests` library
- Open-Meteo Geocoding API
- Open-Meteo Weather Forecast API

## Python Concepts Used

- Functions
- Conditional statements
- While loops
- User input validation
- API integration
- JSON data processing
- Exception handling

## Installation

Make sure Python 3 is installed.

Install the required library using the terminal:

```bash
python -m pip install requests
```

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open `weather_app.py`.
3. Click **Run Python File** or execute:

```bash
python weather_app.py
```

4. Enter a city name, such as Chennai.
5. Wait for the weather information to appear.
6. Enter Yes to check another city or No to exit.

**Note:** An active internet connection is required.

## Sample Output

```text
===== BASIC WEATHER APP =====

Enter city name: Chennai

===== CURRENT WEATHER =====
City: Chennai
Temperature: 29.5 °C
Temperature: 85.1 °F
Humidity: 74%
Weather Condition: Partly Cloudy or Cloudy
Wind Speed: 12.4 km/h
===========================

Check another city? (yes/no): no

Thank you for using Weather App!
```

*The values above are illustrative. Actual weather data changes according to the API response.*

## API Information

The project uses two free Open-Meteo services:

1. Geocoding API – Converts a city name into latitude and longitude.
2. Weather Forecast API – Retrieves current temperature, humidity, weather conditions, and wind speed.

No API key is required for this project.

## Conclusion

This project demonstrates how to integrate an external weather API with Python. It provides practical experience with HTTP requests, JSON processing, user input validation, and error handling.