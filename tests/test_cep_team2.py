from src.consulta_cepformatado import get_cepFormatado
from src.consulta_cep import get_cep

def test_logradouro():
    data1 = get_cep("11015002")
    assert data1['logradouro'] == "Avenida Conselheiro Nébias"
    data1 = get_cep("11075500")
    assert data1['logradouro'] == "Rua Princesa Isabel"

def test_bairro():
    data1 = get_cep("11015002")
    assert data1['bairro'] == "Vila Mathias"
    data1 = get_cep("11075500")
    assert data1['bairro'] == "Vila Belmiro"

def test_cepinvalido():
    data1 = get_cep("00000000")
    assert "erro" in data1

def test_enderecoformatado():
    data1 = get_cepFormatado("01001000")
    assert data1 == "Praça da Sé, Sé - São Paulo / SP"



