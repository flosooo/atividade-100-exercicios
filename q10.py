# Questão 10:  Faça um algoritmo que leia a largura e altura de uma parede, calcule e
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

altura_parede = float(input("Informe o altura da parede: "))
largura_parede = float(input("Informe o largura da parede: "))
area_pintar = altura_parede * largura_parede
print(f"Área a ser pintada: {area_pintar}, quantidade de litros de tinta: {area_pintar / 2}")