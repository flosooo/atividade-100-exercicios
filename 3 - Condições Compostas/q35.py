# Questão 35: Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
# aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
# carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
# que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
# quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
# tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km

carro = input("Qual o tipo de carro alugado (popular ou luxo)? ")
dias = int(input("Quantos dias de aluguel? "))
km = float(input("Quantos Km foram percorridos? "))
if carro == "popular":
  if km <= 100:
    preco = 90 * dias + 0.20 * km
  else:
    preco = 90 * dias + 0.10 * km
elif carro == "luxo":
  if km <= 200:
    preco = 150 * dias + 0.30 * km
  else:
    preco = 150 * dias + 0.25 * km
else:
  print("Tipo de carro inválido")
print(f"O preço a ser pago é R${preco:.2f}")
