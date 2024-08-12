# Questão 80: Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e
# 15 sorteados pelo computador. Depois disso, peça para o usuário digitar um
# número (chave) e seu programa deve mostrar em que posições essa chave foi
# encontrada. Mostre também quantas vezes a chave foi sorteada.

import random

vetor = []
pos = []
for i in range(30):
  vetor.append(random.randrange(1, 15))

key = int(input('Digite a chave: '))

print(vetor)
for i in range(len(vetor)):
  if vetor[i] == key:
    print(f'{i+1}°', end=' ')
    pos.append(i+1)
  else:
    print('X',end=' ')

print('\n' * 2)
print('Os números chave estão nas posições: ', ', '.join(map(str, pos)))
print(f'A chave foi sorteada {len(pos)} vezes')