# Questão 46: Crie um programa que calcule e mostre na tela o resultado da soma entre 6 +
# 8 + 10 + 12 + 14 + ... + 98 + 100.
soma = 0
for i in range(6, 101, 2):
    soma += i
print(f'A soma total é: {soma}')
