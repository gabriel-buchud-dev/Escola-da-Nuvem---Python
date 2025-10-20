'''Função para verificar palíndromo'''

import string

def verificar_palindromo(texto: str) -> bool:
    """Verifica se a palavra ou frase é um palíndromo, ignorando espaços e pontuação."""
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

# Exemplo de uso
frase = input("Digite uma palavra ou frase: ")
if verificar_palindromo(frase):
    print("Sim")
else:
    print("Não")
