# Questão 70: Faça um programa que mostre os 10 primeiros elementos da Sequência 
# de Fibonacci: 1 1 2 3 5 8 13 21...
a,b = 1, 1
for i in range(10):
  print(a, end=' ')
  a,b = b, a+b