from src.consulta_cep import getCep

def test_logradouro():
    data1 = getCep("11015002")
    assert data1['logradouro'] == "Avenida Conselheiro Nébias"
    data1 = getCep("11075500")
    assert data1['logradouro'] == "Rua Princesa Isabel"

def test_bairro():
    data1 = getCep("11015002")
    assert data1['bairro'] == "Vila Mathias"
    data1 = getCep("11075500")
    assert data1['bairro'] == "Vila Belmiro"

def test_cepinvalido():
    data1 = getCep("00000000")
    assert "erro" in data1
