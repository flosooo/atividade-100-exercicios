# Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
# para todos, mas especialmente para mulheres. Faça um programa que leia nome,
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que: 
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

nome = input("Digite o nome do cliente: ")
sexo = input("Digite o sexo do cliente: ")
valor = float(input("Digite o valor das compras do cliente: "))
if sexo.lower().startswith("fem"):
  valor = valor - (valor * 0.13)
elif sexo.lower().startswith("mas"):
  valor = valor - (valor * 0.05)
else:
  print("Nenhum desconto pôde ser aplicado.")
print(f"{nome.capitalize()}, seu valor a pagar com desconto é: R${round(valor, 2)}")
