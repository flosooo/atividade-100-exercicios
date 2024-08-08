# Questão 39: Faça um algoritmo que mostre na tela a seguinte contagem:
# 10 9 8 7 6 5 4 3 Acabou!
import time

for i in range(10, 2, -1):
  print(i)
  time.sleep(.5)
print('Acabou!')
