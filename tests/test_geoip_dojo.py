from src.consulta_geoip_dojo1 import get_geoip, get_lat_long

def test_geoip_ip():
    data = get_geoip("201.28.235.5")
    assert data["ip"] == "201.28.235.5"

def test_geoip_ipinvalido():
    data = get_geoip("000.000.000")
    assert data["ip"] == "0.0.0.0"
    data = get_geoip("0")
    asssert = data["ip"] == "0.0.0.0"

def test_geoip_country_name():
    data = get_geoip("201.28.235.5")
    assert data['country_name'] == "Brazil"

def test_lat_long():
    data = get_two_ip("201.28.235.5", "200.155.115.162")
    geo_distance =  {'201.28.235.5': {'latitude' : -22.8305, 'longitude': -43.2192},
                    '200.155.115.162': {'latitude' : -23.8566, 'longitude': -46.2705}}
    # data1 = get_geoip("201.28.235.5")
    # geo_distance1 = { 'latitude' : -22.8305, 'longitude': -43.2192}
    # data2 = get_geoip("200.155.115.162")
    # geo_distance2 = { 'latitude' : -23.8566, 'longitude': -46.2705}
    assert get_lat_long(data) == geo_distance
    

    

