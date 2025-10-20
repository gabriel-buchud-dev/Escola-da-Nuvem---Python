'''Programa de conversão de moedas'''

valor_reais = float(input("Digite o valor em reais: R$ "))
taxa_dolar = float(input("Digite a cotação atual do dólar: R$ "))
taxa_euro = float(input("Digite a cotação atual do euro: R$ "))

valor_em_dolar = valor_reais / taxa_dolar
valor_em_euro = valor_reais / taxa_euro

print("\n--- Conversor de Moeda ---")
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Taxa do Dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do Euro: R$ {taxa_euro:.2f}")
print("-" * 30)
print(f"Valor em Dólar: $ {valor_em_dolar:.2f}")
print(f"Valor em Euro: € {valor_em_euro:.2f}")
