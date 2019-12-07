import requests

def get_cep(cep):
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    print(resposta.json())
    return resposta.json()


def concat(body): 
    return f"{body['logradouro']}, {body['bairro']} - {body['localidade']} / {body['uf']}"


def main():
    get_cep('11010151')

if __name__ == "__main__":
    main()