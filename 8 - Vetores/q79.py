# Questão 79: Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor.
# No final, mostre quais são os números pares que foram digitados e em que
# posições eles estão armazenados.

vetor = []
pos = []
for i in range(10):
  num = int(input('Digite um número: '))
  vetor.append(num)
print(vetor)

for i in range(len(vetor)):
  if vetor[i] % 2 == 0:
    print(f'{i+1}°', end=' ')
    pos.append(i+1)
  else:
    print('X',end=' ')
    
print('\n' * 2)
print('Os números pares estão nas posições: ', ', '.join(map(str, pos)))