from src.consulta_cep_dojo1 import get_cep, concat


def test_rua():
    result = get_cep("11010151")
    nome_rua = "Rua Quinze de Novembro"
    assert result['logradouro'] == nome_rua

def test_rua_bairro_cidade_uf():
    result = get_cep("11010151")
    rua_bairro_cidade = "Rua Quinze de Novembro, Centro - Santos / SP"
    assert concat(result) == rua_bairro_cidade








"""from src.consulta_cep import get_cep

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
"""