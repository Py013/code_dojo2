import requests 

''' consome  a API de https://tools.keycdn.com/geo'''
def get_geoip(ip):
    request = requests.get("https://tools.keycdn.com/geo.json?host={}".format(ip))
    data = request.json()['data']
    return data['geo']

def get_lat_long(body):
    return {'latitude': body['latitude'], 'longitude': body['longitude']}

def get_two_ip(ip1, ip2):
    result_ip1 = get_geoip(ip1) 
    #Ficou pendente criar função que pesquisa os dois Ips
    #devolve a long e lat dos dois

def main():
    # print(get_geoip("201.28.235.5"))
    # print(get_geoip("000.000.000"))
    geo = get_geoip("201.28.235.5")
    ip = geo['ip']
    # print(ip)

if __name__ == "__main__":
    main()
