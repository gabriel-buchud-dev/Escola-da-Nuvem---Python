'''Calculadora de Desconto '''

produtos = {
    1: {"nome": "Camiseta", "preco": 50.00},
    2: {"nome": "Calça", "preco": 120.00},
    3: {"nome": "Jaqueta", "preco": 200.00}
}

print("--- Menu de Produtos ---")
for chave, produto in produtos.items():
    print(f"{chave} - {produto['nome']} (R$ {produto['preco']:.2f})")

escolha = int(input("Escolha o produto pelo número: "))

if escolha in produtos:
    produto_escolhido = produtos[escolha]
    porcentagem_desconto = 20
    valor_desconto = produto_escolhido["preco"] * (porcentagem_desconto / 100)
    preco_final = produto_escolhido["preco"] - valor_desconto

    print("\n--- Detalhes do Produto ---")
    print(f"Produto: {produto_escolhido['nome']}")
    print(f"Preço original: R$ {produto_escolhido['preco']:.2f}")
    print(f"Desconto: {porcentagem_desconto}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")
else:
    print("Opção inválida.")
