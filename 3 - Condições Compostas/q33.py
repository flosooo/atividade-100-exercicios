# Questão 33: Escreva um programa para aprovar ou não o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos você vai pagar o imóvel: "))

prestacao = valor_casa / (anos * 12)
if prestacao > (salario * 0.3):
  print("Empréstimo negado!")
else:
  print("Empréstimo aprovado!")
