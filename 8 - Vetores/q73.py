# Questão 73: Crie um programa que preencha automaticamente (usando lógica, não apenas
# atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
# 9 8 7 6 5 4 3 2 1 0
# 0 1 2 3 4 5 6 7 8 9
vetor = []
for i in range(9, -1, -1):
    vetor.append(i)

indices = list(range(len(vetor)))
print(vetor)
print(indices)