'''Conversor de Temperatura'''

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F ou K): ").upper()

if unidade_origem == "C":
    temp_c = temperatura
elif unidade_origem == "F":
    temp_c = (temperatura - 32) * 5/9
elif unidade_origem == "K":
    temp_c = temperatura - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

if unidade_destino == "C":
    resultado = temp_c
elif unidade_destino == "F":
    resultado = temp_c * 9/5 + 32
elif unidade_destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida.")
    exit()

print(f"{temperatura:.2f}{unidade_origem} equivalem a {resultado:.2f}{unidade_destino}")
