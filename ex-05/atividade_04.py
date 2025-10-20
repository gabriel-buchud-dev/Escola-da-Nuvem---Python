'''Calculadora de Dias Vividos'''

from datetime import datetime

data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

data_atual = datetime.today()

dias_vividos = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vividos} dias.")
