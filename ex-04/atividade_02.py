'''Registro de Notas e Cálculo da Média da Turma'''

quantidade_alunos = int(input("Digite o número de alunos na turma: "))

soma_notas = 0

for i in range(1, quantidade_alunos + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    soma_notas += nota

media_turma = soma_notas / quantidade_alunos

print(f"\nA média da turma é: {media_turma:.2f}")
