import requests
from pprint import pprint
import geopy.distance

api_call_lat = 'http://api.openweathermap.org/data/2.5/find?lat=-23.45&lon=-46.64&cnt=50'
api_key  = 'appid=d143fc16834aca6593ac42af685b0866'
# api_key  = 'appid=<put you API key here>'
#api_key  = 'appid=b6907d289e10d714a6e88b30761fae22'

def Convert2Celcius(temp):
    return temp - 273.15

def Convert2Fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32


def main():
    print('The Weather APP')
    print('---------------')
        
    url_lat = api_call_lat + '&' + api_key

    coords_1 = (-23.55, -46.64)
    coords_2 = (-10.90, -37.07)

    distance = geopy.distance.distance(coords_1, coords_2).km

    print(f'A distancia entre as duas cidades de Aracaju e São Paulo é de {distance}')

    r = requests.get(url_lat)

    if r.ok:
        weather_info = r.json()
        pprint(weather_info)
    else :
        print('Error {}'.format(r.reason))

if __name__ == "__main__":
    main()