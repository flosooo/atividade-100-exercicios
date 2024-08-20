# Questão 69: Desenvolva um programa que leia o primeiro termo e a razão de uma
# PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e
# a soma entre todos os valores da sequência.

termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
soma = 0
for i in range(termo1, termo1 + 10*razao, razao):
  print(i)
  soma +=i
print(f'A soma dos termos da PA é: {soma}')