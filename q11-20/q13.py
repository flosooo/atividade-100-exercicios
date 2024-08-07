# Questão 13: Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o  seu novo salário, com 15% de aumento

salario = float(input("Digite o salário: "))
print(f"Com o aumento de 15%, o novo salário será: R${round(salario * 1.15, 2)}")
