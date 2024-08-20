# Questão 63: Crie um programa usando a estrutura “faça enquanto” que leia vários números.
# A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na
# tela:
# a) O somatório entre todos os valores
# b) Qual foi o menor valor digitado
# c) A média entre todos os valores
# d) Quantos valores são pares

num = []
pares = 0
while True:
  entrada = int(input('Digite um número: '))
  num.append(entrada)
  r = input('Deseja continuar? [S/N] ')
  if r == "N":
    break

for i in num:
  if i % 2 == 0:
    pares += 1

print(f'A soma entre todos os valores é {sum(num)}')
print(f'O menor valor digitado foi {min(num)}')
print(f'A média entre todos os valores é {sum(num)/len(num):.2f}')
print(f'A quantidade de valores pares é {pares}')
