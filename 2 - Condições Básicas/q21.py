# Questão 21: Faça um algoritmo que leia um determinado ano e mostre se ele é ou não  BISSEXTO. 
numero = int(input("Digite um ano: "))
if numero % 4 == 0:
  print("O ano é bissexto")
else: 
  print("Não é um ano bissexto")
