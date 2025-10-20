'''Consulta de CEP via API'''

import requests

cep = input("Digite o CEP (somente números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("--- Informações do CEP ---")
        print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
        print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
        print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
        print(f"Estado: {dados.get('uf', 'Não disponível')}")

except requests.RequestException:
    print("Falha ao consultar o CEP. Verifique sua conexão ou tente novamente mais tarde.")
