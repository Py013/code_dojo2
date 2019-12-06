from src.contulta_geoip import get_geoip

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