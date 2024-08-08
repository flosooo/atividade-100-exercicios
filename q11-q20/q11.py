# Questão 11: Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.

a = int(input('Digite o valor que acompanha X²: '))
b = int(input('Digite o valor que acompanha X: '))
c = int(input('Digite o valor isolado: '))

print(f"O valor de delta é: {(b**2) - (4*a*c)}")
