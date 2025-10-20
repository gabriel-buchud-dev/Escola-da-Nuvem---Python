'''Calculadora de Consumo de Combustível'''

distancia = float(input("Digite a distância percorrida em km: "))
combustivel = float(input("Digite a quantidade de combustível gasto em litros: "))

consumo_medio = distancia / combustivel

print("\n--- Consumo de Combustível ---")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Combustível gasto: {combustivel:.2f} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
