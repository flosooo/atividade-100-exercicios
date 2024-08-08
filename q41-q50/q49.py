# Questão 49: Crie um programa que leia 6 números inteiros e no final mostre quantos deles
# são pares e quantos são ímpares.
lista = []

for i in range(6):
    lista.append(int(input('Digite um número: ')))

pares = []
impares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
      
print(f'Números pares: {pares}. Total de números pares: {len(pares)}')
print(f'Números ímpares: {impares}. Total de números ímpares: {len(impares)}')
