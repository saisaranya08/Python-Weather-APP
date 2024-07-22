


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

API_KEY = 'git '  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
BACKGROUND_IMAGE_PATH = "C:/Users/91709/Downloads/bgimg.webp"

def get_weather(city):
    """Fetches weather data from OpenWeatherMap API."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric' 
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def show_weather():
    """Displays weather information."""
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data:
        main = weather_data['main']
        weather = weather_data['weather'][0]
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']

        result = f"City: {city.capitalize()}\nTemperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {description.capitalize()}"
        weather_label.config(text=result)
    else:
        messagebox.showerror("Error", "City not found or invalid API key")

# Setting up the user interface
app = tk.Tk()
app.title("Weather App")

# background image
background_image = Image.open("C:/Users/91709/Downloads/bgimg.webp")
background_image = background_image.resize((1500, 1300), Image.LANCZOS) 
bg_image = ImageTk.PhotoImage(background_image)

bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

#font size and type
font = ('Times New Roman', 16)

# Create a frame 
frame = tk.Frame(app, bg='#E6E6FA', padx=80, pady=80)
frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(frame, text="Enter City:", bg='#E6E6FA', font=font).pack(pady=12)
city_entry = tk.Entry(frame, font=font)
city_entry.pack(pady=5)

tk.Button(frame, text="Get Weather", command=show_weather, font=font).pack(pady=10)

weather_label = tk.Label(frame, text="", bg='#E6E6FA', font=('Times New Roman', 16), justify=tk.LEFT)
weather_label.pack(pady=18)

# Center align the window
app.update_idletasks()
width = app.winfo_width()
height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
app.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

# Run the app
app.mainloop()


