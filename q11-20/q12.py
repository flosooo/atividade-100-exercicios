# Questão 12: Crie um programa que leia o preço de um produto, calcule e mostre o seu  PREÇO PROMOCIONAL, com 5% de desconto. 
preco = float(input("Digite o preço do produto: "))
desconto = preco - (preco * 0.05)
print(f"Com o preço promocional de 5%, o produto custará: R${desconto:.2f}")
