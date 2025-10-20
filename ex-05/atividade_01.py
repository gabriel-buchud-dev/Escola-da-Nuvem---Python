'''Função para calcular gorjeta'''

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """Gorjeta com base na conta e na porcentagem desejada."""
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = float(input("Digite o valor total da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))

valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"O valor da gorjeta é: R$ {valor_gorjeta:.2f}")
