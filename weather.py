from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfiled.get()

        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p ")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

   

#weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=37515154dff8a8cceca6bededb460b83"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalide Entry!!!")





#search box
Search_imagine=PhotoImage(file="Weatherapp/search.png")
myimagine=Label(image=Search_imagine)
myimagine.place(x=20,y=20)

textfiled=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfiled.place(x=50,y=40)
textfiled.focus()

Search_icon=PhotoImage(file="Weatherapp/search_icon.png")
myimagine_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimagine_icon.place(x=400,y=34)

#logo

Logo_image=PhotoImage(file="Weatherapp/logo.png")
logo=Label(image=Logo_image)
logo.place(x=150, y=100)

#Bottom box :
Frame_imagine=PhotoImage(file="Weatherapp/box.png")
frame_myimagine=Label(image=Frame_imagine)
frame_myimagine.pack(padx=5,pady=5,side=BOTTOM)

#time

name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#Label
label=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label.place(x=120,y=400)

labe2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
labe2.place(x=250,y=400)

labe3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
labe3.place(x=430,y=400)


labe4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
labe4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)


w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ed")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ed")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ed")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ed")
p.place(x=670,y=430)















root.mainloop()
