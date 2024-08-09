# Questão 78: Escreva um programa que leia 15 números e guarde-os em um vetor. No final,
# mostre o vetor inteiro na tela e em seguida mostre em que posições foram
# digitados valores que são múltiplos de 10.

vetor = []
pos = []
for i in range(15):
  num = int(input('Digite um número: '))
  vetor.append(num)
print(vetor)

for i in range(len(vetor)):
  if vetor[i] % 10 == 0:
    print(f'{i+1}°', end=' ')
    pos.append(i+1)
  else:
    print('X',end=' ')
print('\n' * 2)

print('Os números múltiplos de 10 estão nas posições: ', ', '.join(map(str, pos)))