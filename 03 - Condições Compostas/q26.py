# Questão 26: Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
# na tela uma das mensagens abaixo:
# - O primeiro valor é o maior
# - O segundo valor é o maior
# - Não existe valor maior, os dois são iguais
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um outro número: '))
if num1 > num2:
  print('O primeiro valor é o maior.')
elif num2 > num1:
  print('O segundo valor é o maior')
else:
  print('Não existe valor maior, os dois são iguais.')
