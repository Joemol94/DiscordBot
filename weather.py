import os
import requests
from pprint import pprint
import pandas as pd

def get_weather(txt):
    API_KEY = os.environ['API_KEY']
    #div,city  = txt.split(' ')
    #city = input('Enter a city: ')
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+txt
    weather_data = requests.get(base_url).json()
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    temp = weather_data['main']['temp']
    temp_max = weather_data['main']['temp_max']
    temp_min = weather_data['main']['temp_min']
    description = weather_data['weather'][0]['description']
    d1 = {'Particulars':['Description','Temperature','Feels-like','Max_Temp','Min_Temp','Humidity'],
            'Values':[description,temp,feels_like,temp_max,temp_min,humidity]}
    df = pd.DataFrame(d1)
    df = df.to_string(index=False)
    #print(df)
    return df

#get_weather('weather chennai')