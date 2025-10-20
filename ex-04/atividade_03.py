'''Verificador de Segurança de Senha'''

senha = input("Digite uma senha: ")

# Critérios básicos
tamanho_valido = len(senha) >= 8
tem_numero = any(c.isdigit() for c in senha)

# Critérios extras de segurança
tem_maiuscula = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_caractere = any(not c.isalnum() for c in senha)

if tamanho_valido and tem_numero:
    print("Senha atende aos critérios básicos.")
    if tem_maiuscula and tem_minuscula and tem_caractere:
        print("Senha também é considerada segura (contém maiúsculas, minúsculas e caracteres especiais).")
    else:
        print("Para maior segurança, inclua letras maiúsculas, minúsculas e caracteres especiais.")
else:
    print("Senha inválida. Certifique-se de que tenha pelo menos 8 caracteres e pelo menos um número.")
