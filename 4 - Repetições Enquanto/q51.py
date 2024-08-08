# Questão 51: Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela
# qual foi o maior e qual foi o menor preço digitados.

precos = []
for i in range(8):
  preco = float(input(f"Digite o preço do produto {i+1}: "))
  precos.append(preco)
  
print(f'O maior preço é: {max(precos)}, \n e o menor preço é: {min(precos)}')
# ou
# for preco in precos:
#   if preco > maior_preco:
#       maior_preco = preco
#           print('O maior preço é: ', maior_preco')
#   if preco < menor_preco:
#       menor_preco = preco
#         print('O maior preço é: ', maior_preco')