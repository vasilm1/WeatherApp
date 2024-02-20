from requests import get
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap
from ttkbootstrap import Style

GMAP_API = ''
GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

WEATHER_API = ''
WEATHER_URL = 'http://api.weatherapi.com/v1/current.json'


def geocode():
    area = str(location.get())
    area = area.replace(" ", "%20")
    url = f"{GEOCODE_URL}?address={area}&key={GMAP_API}"
    data = get(url).json()

    if data['status'] == "ZERO_RESULTS":
        messagebox.showerror("Error", "Invalid City, please try specifying country/state.")
        return None

    data = data['results'][0]['geometry']['location']

    return (getweather(data))


def getweather(coordinates):
    latitude = coordinates['lat']
    longitude = coordinates['lng']
    url = f"{WEATHER_URL}?key={WEATHER_API}&q={latitude},{longitude}&days=1&aqi=yes&alerts=no"
    data = get(url).json()
    city = data['location']['name']

    # pprint.pprint(data)  # testing

    data = data['current']
    condition = data['condition']['text']
    iconurl = data['condition']['icon']
    temperature = data['temp_c']
    feelslike = data['feelslike_c']
    humidity = data['humidity']
    uv = data['uv']
    isday = data['is_day']

    # airquality = data['air_quality'] #chose not to use

    return (iconurl, city, condition, temperature, feelslike, humidity, uv, isday)


def main():
    info = geocode()
    iconurl, city, condition, temperature, feelslike, humidity, uv, isday = info

    icon = Image.open(get("https:" + iconurl, stream=True).raw)
    icon = ImageTk.PhotoImage(icon)

    if isday == 1:
        style = Style(theme='morph')
    else:
        style = Style(theme='superhero')

    locationlabel.configure(text=city)
    conditionlabel.configure(text=condition)
    iconlabel.configure(image=icon)
    iconlabel.image = icon
    templabel.configure(text=str(temperature) + " C°")
    feelslikelabel.configure(text=f"Feels like {feelslike} C°")
    humiditylabel.configure(text="Humidity " + str(humidity) + "%")
    uvlabel.configure(text="UV Index: " + str(uv))


style = Style(theme='lumen')

window = style.master
window.title("Weather")
window.geometry("400x500")

location = ttkbootstrap.Entry(window, font="Merriweather, 18")
location.pack(pady=10)

search = ttkbootstrap.Button(window, text="Search", command=main, bootstyle="warning")
search.pack(pady=10)

iconlabel = tk.Label(window)
iconlabel.pack()

locationlabel = tk.Label(window, font="Merriweather, 25")
locationlabel.pack(pady=20)

conditionlabel = tk.Label(window, font="Merriweather, 20")
conditionlabel.pack()

templabel = tk.Label(window, font="Merriweather, 20")
templabel.pack()

feelslikelabel = tk.Label(window, font="Merriweather, 20")
feelslikelabel.pack()

humiditylabel = tk.Label(window, font="Merriweather, 20")
humiditylabel.pack()

uvlabel = tk.Label(window, font="Merriweather, 20")
uvlabel.pack()

window.mainloop()