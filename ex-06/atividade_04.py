'''Consulta de Cotação do Real via API'''

import requests
from datetime import datetime

print()
moeda = input("Digite a sigla da moeda (ex: USD, EUR): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    par_chave = f"{moeda}BRL"
    if par_chave in dados:
        info = dados[par_chave]
        valor_atual = float(info['bid'])
        valor_max = float(info['high'])
        valor_min = float(info['low'])
        timestamp = int(info['timestamp'])
        data_hora = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print()
        print(f"--- Cotação {moeda} / BRL ---")
        print()
        print(f"Valor atual: R$ {valor_atual:.2f}")
        print(f"Máxima: R$ {valor_max:.2f}")
        print(f"Mínima: R$ {valor_min:.2f}")
        print(f"Última atualização: {data_hora}")
    else:
        print("Moeda não encontrada.")

except requests.RequestException:
    print("Falha na requisição. Verifique sua conexão ou tente novamente mais tarde.")
