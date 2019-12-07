from src.consulta_geoip import *
import geopy.distance

#
# def test_geoip_ip():
#     data = get_geoip("201.28.235.5")
#     assert data["ip"] == "201.28.235.5"
#
# def test_geoip_ipinvalido():
#     data = get_geoip("000.000.000")
#     assert data["ip"] == "0.0.0.0"
#     data = get_geoip("0")
#     asssert = data["ip"] == "0.0.0.0"
#
# def test_geoip_country_name():
#     data = get_geoip("201.28.235.5")
#     assert data['country_name'] == "Brazil"

def test_geoip_latlong():
    data = get_geoip_lat_long("13.227.101.96")
    assert data == (47.6348, -122.3451)

def test_distance():
    distancia = get_geo_distance("13.227.101.96","201.28.235.5")
    assert distancia == 11078.97456229238

