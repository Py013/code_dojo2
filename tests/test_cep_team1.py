from src.consulta_cep_dojo1 import get_cep, concat


def test_rua():
    result = get_cep("11010151")
    nome_rua = "Rua Quinze de Novembro"
    assert result['logradouro'] == nome_rua

def test_rua_bairro_cidade_uf():
    result = get_cep("11010151")
    rua_bairro_cidade = "Rua Quinze de Novembro, Centro - Santos / SP"
    assert concat(result) == rua_bairro_cidade
