'''Classificador de Números: Par ou Ímpar'''

quantidade = int(input("Quantos números você quer analisar? "))

pares = 0
impares = 0

for i in range(1, quantidade + 1):
    numero = int(input(f"Digite o número {i}: "))
    if numero % 2 == 0:
        print(f"{numero} é par.")
        pares += 1
    else:
        print(f"{numero} é ímpar.")
        impares += 1

print("\n--- Resultado ---")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
