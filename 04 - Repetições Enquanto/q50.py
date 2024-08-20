# Questão 50: Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e
# mostre na tela:
# a) Quais foram os números sorteados
# b) Quantos números estão acima de 5
# c) Quantos números são divisíveis por 3
import random

lista = []
for i in range(0, 21, 1):
  random.randrange(0,10)
  lista.append(random.randrange(0,10))

acima5 = []
div3 = []

for i in lista:
  if i > 5:
    acima5.append(i)
  if i % 3 == 0:
    div3.append(i)
    
print(f'Os números sorteados foram: {lista}\n')
print(f'Os números acima de 5 são: {acima5}\n')
print(f'Os números divisíveis por 3 são: {div3}')
