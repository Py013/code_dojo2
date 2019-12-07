import requests 
from pprint import pprint 
import math

''' consome  a API de https://tools.keycdn.com/geo'''
def get_geoip(ip):
    request = requests.get("https://tools.keycdn.com/geo.json?host={}".format(ip))
    data = request.json()['data']
    return data['geo']

def main():
    # print(get_geoip("201.28.235.5"))
    # print(get_geoip("000.000.000"))
    geo = get_geoip("189.34.240.10")
    ip = geo
    pprint(ip)

if __name__ == "__main__":
    main()