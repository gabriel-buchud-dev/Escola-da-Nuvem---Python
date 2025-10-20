'''Verificador de Ano Bissexto'''

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    resultado = "bissexto"
else:
    resultado = "não bissexto"

print(f"O ano {ano} é {resultado}.")
