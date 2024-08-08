# Questão 28: Faça um programa que leia a largura e o comprimento de um terreno
# retangular, calculando e mostrando a sua área em m2. O programa também
# devemostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m2 = TERRENO POPULAR
# - Entre 100m2 e 500m2 = TERRENO MASTER
# - Acima de 500m2 = TERRENO VIP

Largura = float(input("Digite a largura do terreno: "))
Comprimento = float(input("Digite o comprimento do terreno: "))
Area = abs(Largura * Comprimento)
if Area >= 500:
  print('O terreno ultrapassa os 500m2, logo é considerado VIP')
elif Area <= 100:
  print('O terreno é menor que 100m2, logo é considerado POPULAR')
else:
  print('O terreno é maior que 100m2 mas menor que 500m2, logo é considerado MASTER')
