'''Classificador de Idade'''

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"Você se enquadra na categoria: {categoria}")
