import requests
from plyer import notification
import time

# Function to fetch weather data
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data")
        return None

# Function to show notification
def show_notification(weather_data, city):
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    notification_title = f"Weather Update for {city}"
    notification_message = (
        f"Temperature: {temperature}°C\n"
        f"Weather: {weather_description.capitalize()}\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} m/s"
    )
    
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=10  # Notification duration in seconds
    )

def main():
    api_key = "18e675970b20afcfac19af949b6d9af0"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")

    # Set interval in seconds
    interval = 3600  # 1 hour

    while True:
        weather_data = get_weather(api_key, city)
        if weather_data:
            show_notification(weather_data, city)
        time.sleep(interval)

if __name__ == "__main__":
    main()
'''import tkinter as tk
from tkinter import messagebox
import requests
def get_weather(city_name, api_key):
    try:
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")
        return None
def show_weather():
    city_name = city_entry.get()
    api_key = "18e675970b20afcfac19af949b6d9af0"  # Replace with your OpenWeatherMap API key
    if not city_name:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    weather_data = get_weather(city_name, api_key)
    if weather_data and weather_data.get("cod") != "404":
        main = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_info = f"City: {city_name}\nTemperature: {temp}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_desc}"
        messagebox.showinfo("Weather Information", weather_info)
    else:
        messagebox.showerror("Error", "City Not Found")
root = tk.Tk()
root.title("Live Weather Notifications")
root.geometry("400x200")

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)
notify_button = tk.Button(root, text="Get Weather", command=show_weather)
notify_button.pack(pady=10)
root.mainloop()'''