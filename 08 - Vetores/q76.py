# Questão 76: Crie um programa que preencha automaticamente um vetor numérico com 7
# números gerados aleatoriamente pelo computador e depois mostre os valores
# gerados na tela.
import random

vetor = []
for i in range(7):
  vetor.append(random.randrange(0, 100))
indices = list(range(len(vetor)))
print(vetor)
print(indices)