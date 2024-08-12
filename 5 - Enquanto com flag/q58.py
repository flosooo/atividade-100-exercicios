# Questão 58: Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa
# vai parar quando for digitada a idade 999. No final, mostre quantos alunos
# existem na turma e qual é a média de idade do grupo.

idade_total = 0
qtd_alunos = 0

while True:
    alunos_idade: int = int(input('Qual a idade do aluno? '))
    idade_total += alunos_idade
    qtd_alunos += 1
    if alunos_idade == 999:
        break

print(f"Quantidade de alunos: {qtd_alunos}, Média da idade do grupo: {idade_total / qtd_alunos}.")

