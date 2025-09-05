import tkinter as tk
from tkinter import messagebox
import requests


def get_weather(city):
    """Fetches weather data from OpenWeatherMap API."""
    api_key = "YOUR_API_KEY"  # <-- IMPORTANT: Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # units=metric for Celsius

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)
        weather_data = response.json()

        # Extract relevant data
        city_name = weather_data['name']
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        result_str = f"City: {city_name}\nTemperature: {temp}°C\nDescription: {description.capitalize()}"
        result_label.config(text=result_str)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to connect to the weather service: {e}")
    except KeyError:
        messagebox.showerror("Error", f"Could not find weather data for '{city}'. Please check the city name.")


# --- UI Setup ---
window = tk.Tk()
window.title("Weather App")
window.geometry("350x200")

tk.Label(window, text="Enter City Name:", font=("Helvetica", 14)).pack(pady=5)

city_entry = tk.Entry(window, font=("Helvetica", 12), width=20)
city_entry.pack(pady=5)

search_button = tk.Button(window, text="Get Weather", command=lambda: get_weather(city_entry.get()))
search_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 12), justify=tk.LEFT)
result_label.pack(pady=10)

window.mainloop()