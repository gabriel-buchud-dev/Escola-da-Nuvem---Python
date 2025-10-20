'''Busca de Usuário Aleatório via Random User API'''

import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("--- Usuário Aleatório ---")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

except requests.RequestException:
    print("Falha ao acessar a API. Verifique sua conexão ou tente novamente mais tarde.")

# Caso não funcione use o comando pip3 install requests, para instalar as dependências corretas.
