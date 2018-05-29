#!/usr/bin/python2.7

import sys
import requests
import tkinter as tk

root = tk.Tk()
root.geometry("480x320")
root.title('Weather check')

API_KEY = 'insert your key'

def weatherReq():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city.get()+'&lang=it&units=metric&appid='+API_KEY)

    temp = str(r.json()['weather'][0]['description'])
    temperature = str(r.json()['main']['temp'])
    min_temperature = str(r.json()['main']['temp_min'])
    max_temperature = str(r.json()['main']['temp_max'])
    humidity = str(r.json()['main']['humidity'])
    wind_speed = str(r.json()['wind']['speed'])

    result.set('Actual weather: ' + temp + '\n'  
    + 'Temperature: ' + temperature + '°C ' + 'Min: ' + min_temperature + '°C ' + 'Max: ' + max_temperature + '°C' + '\n'
    + 'Humidity: ' + humidity + '%' +'\n' 
    + 'Wind speed: ' + wind_speed + 'm/s' )
    print(r.json())

city = tk.StringVar()
result = tk.StringVar()

title_label = tk.Label(text='Insert city').pack(pady=10)
city_box = tk.Entry(root, textvariable=city).pack(pady=10)
exe_buttom = tk.Button(root, text="Tell me the weather", command=weatherReq).pack()

result_label = tk.Label(root, textvariable=result).pack()



root.mainloop()