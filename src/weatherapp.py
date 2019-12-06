#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
NAME  : weatherapp.py
AUTHOR: Alexandre Fukaya
DATE  : Wed Dec  4 08:01:25 2019

DESCRIPTION:
    The script connects to Openweathermap weather API and retrieves the weather
    info for a given location - Console.

USAGE:
    Just run it.

DEPENDENCIES:
    Requests

TODO:
    - Create a ZIP to City relationship.

INPROGRESS:
    - None.

CHANGES:
    20191204 - Configuração Inicial.

"""

import requests

api_call = 'http://api.openweathermap.org/data/2.5/weather?q='
api_key  = 'appid=<put you API key here>'
#api_key  = 'appid=b6907d289e10d714a6e88b30761fae22'

def Convert2Celcius(temp):
    return temp - 273.15

def Convert2Fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32

def main():
    print('The Weather APP')
    print('---------------')
    print()
    print('Enter location data.')
    city    = input('City: ').title()
    country = input('Country: ').upper() 
    scale   = input('Degrees: ').upper()
    
    url = api_call + city + ',' + country + '&' + api_key
    
    r = requests.get(url)

    if r.ok:
        weather_info = r.json()
        
        info_temp    = weather_info['main']['temp']
        info_weather = weather_info['weather'][0]['main']
        info_maxtemp = weather_info['main']['temp_max']
        info_mintemp = weather_info['main']['temp_min']

        if scale == 'C' :
            temperature = round(Convert2Celcius(info_temp),1)
            temp_min    = round(Convert2Celcius(info_mintemp),1)
            temp_max    = round(Convert2Celcius(info_maxtemp),1)
        elif scale == 'F':
            temperature = round(Convert2Fahrenheit(info_temp),1)
            temp_min    = round(Convert2Fahrenheit(info_mintemp),1)
            temp_max    = round(Convert2Fahrenheit(info_maxtemp),1)
        else:
            print('Error: Unknown Temperature Scale.')
            return
        
        print()
        print('---------------')
        print('Today\'s weather at {0} is {1}'.format(city,info_weather))
        print('The temperature is {0}º{1}'.format(temperature,scale))
        print('with minimum of {0}º{2} and maximum of {1}º{2}'.format(temp_min,temp_max,scale))
        print('---------------')
        print()
        
    else :
        print('Error {}'.format(r.reason))

if __name__ == "__main__":
    main()