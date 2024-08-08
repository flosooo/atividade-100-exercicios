# Questão 48: Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
soma = 0
for i in range(7):
  num = int(input("Digite um número: "))
  soma += num
print(f"A soma dos números é {soma}")
