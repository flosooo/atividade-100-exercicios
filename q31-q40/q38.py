# Questão 38: Escreva um programa que mostre na tela a seguinte contagem:
# 6 7 8 9 10 11 Acabou!
import time

for i in range(6, 12):
  print(i)
  time.sleep(.5)
print('Acabou!')
