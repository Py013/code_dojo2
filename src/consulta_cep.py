import requests

def getCep(cep):
    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    return request.json()

def main():
    print('### CEP ###')
    cep = input('Digite o CEP..: ')

    if len(cep) != 8:
        print("Entre com 8 digitos de cep sem o traço")
    else:
        dados = getCep(cep)
        if 'erro' in dados:
            print("CEP não encontrado!")
        else:
            print(dados)
            print('Logradouro...: '+dados['logradouro'])
            print('Numero.......: '+dados['complemento'])
            print('Bairro.......: '+dados['bairro'])
            print('Cidade.......: '+dados['localidade'])
            print('Estado.......: '+dados['uf'])

if __name__ == "__main__":
    main()