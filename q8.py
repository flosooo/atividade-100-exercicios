# Questão 8: Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.

distancia_metros = float(input("Informe a distância em metros: "))
print(f"Kilometros: {distancia_metros / 1000}km\n"
      f"Hectometros: {distancia_metros / 100}Hm\n"
      f"Decâmetros: {distancia_metros / 10}Dam\n"
      f"Decímetros: {distancia_metros * 10}Dm\n"
      f"Centimetros: {distancia_metros * 100}Cm\n"
      f"Milímetros: {distancia_metros * 1000}Mm")