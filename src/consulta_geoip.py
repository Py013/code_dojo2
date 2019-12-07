import requests 
import geopy.distance

''' consome  a API de https://tools.keycdn.com/geo'''
def get_geoip(ip):
    request = requests.get("https://tools.keycdn.com/geo.json?host={}".format(ip))
    data = request.json()['data']
    return data['geo']

def get_geoip_lat_long(ip):
    request = requests.get("https://tools.keycdn.com/geo.json?host={}".format(ip))
    data = request.json()['data']['geo']
    return (data['latitude'] , data['longitude'])

def get_geo_distance(ip1, ip2):
    coord1 = get_geoip_lat_long(ip1)
    coord2 = get_geoip_lat_long(ip2)
    return geopy.distance.distance(coord1, coord2).km

def main():
    print(get_geoip("13.227.101.96"))
    print(get_geoip("000.000.000"))
    geo = get_geoip("201.28.235.5")
    ip = geo['ip']
    print(ip)
    print("Distancia entre 13.227.101.96 e 201.28.235.5 = "+str(get_geo_distance("13.227.101.96","201.28.235.5")))

if __name__ == "__main__":
    main()
