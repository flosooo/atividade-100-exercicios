# Questão 17: Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse  80Km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba  o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida

Velocidade = int(input("Qual a velocidade atual do carro?\n"))
if Velocidade > 80:
  print("Você foi multado!")
  multa = (Velocidade - 80) * 5
  print("O valor da multa é de R$", multa)
else:
  print("Você está dentro do limite de velocidade!")
