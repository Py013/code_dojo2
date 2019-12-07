import requests

def get_cepFormatado(cep):
    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    data = request.json()
    return data['logradouro'] + ', ' + data['bairro'] + ' - ' + data['localidade'] + ' / ' + data['uf']

def main():
    print('### CEP ###')
    cep = input('Digite o CEP..: ')

    if len(cep) != 8:
        print("Entre com 8 digitos de cep sem o traço")
    else:
        dados = get_cepFormatado(cep)
        print (dados)
if __name__ == "__main__":
    main()