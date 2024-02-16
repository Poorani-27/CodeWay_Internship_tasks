import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("600x600")

def get_weather(city):
    API_key = "your api key"  # Replace this with your actual API key
    Url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(Url)
    
    if res.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
    
    if res.status_code == 401:  
        messagebox.showerror("Error", "Invalid API Key. Please check your API key.")
        return None
    
    if not res.ok:
        messagebox.showerror("Error", f"Internal Server Error: {res.text}")
        return None
    
    weather = res.json()
    try:
        icon_id = weather['weather'][0]['icon']
        temperature_celsius = weather['main']['temp'] - 273.15  
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32  
        description = weather['weather'][0]['description']
        city_name = weather['name']
        country_code = weather['sys']['country']
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
        return (icon_url, temperature_celsius, temperature_fahrenheit, description, city_name, country_code)
    except KeyError:
        messagebox.showerror("Error", "Invalid response from server")
        return None


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url, temperature_celsius, temperature_fahrenheit, description, city_name, country_code = result
    location_label.config(text=f"{city_name}, {country_code}")
    try:
        image = Image.open(requests.get(icon_url, stream=True).raw)
        icon = ImageTk.PhotoImage(image)
        icon_label.config(image=icon)
        icon_label.image = icon
    except Exception as e:
        messagebox.showerror("Error", f"Error loading icon: {str(e)}")
    temperature_label.config(text=f"Temperature: {temperature_celsius:.2f}°C / {temperature_fahrenheit:.2f}°F")
    description_label.config(text=f"Description: {description}")

city_entry = ttkbootstrap.Entry(root, font=("Helvetica", 18))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="search", command=search, font=("Arial", 20, "bold"))
search_button.pack(pady=10)

location_label = tk.Label(root, font=("Arial", 18, "bold"))
location_label.pack(pady=8)

icon_label = tk.Label(root, font=("Arial", 18, "bold"))
icon_label.pack(pady=8)

temperature_label = tk.Label(root, font=("Arial", 18, "bold"))
temperature_label.pack(pady=8)

description_label = tk.Label(root, font=("Arial", 18, "bold"))
description_label.pack(pady=8)

root.mainloop()
