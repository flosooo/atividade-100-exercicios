# Questão 38: Escreva um programa que mostre na tela a seguinte contagem:
# 6 7 8 9 10 11 Acabou!
def mostrar_numeros(min, max):
  for i in range(min, max):
  print(i)
  print('Acabou!')

mostrar_numeros(6, 12)