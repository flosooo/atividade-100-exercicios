# Questão 18: Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade  dela e depois mostre se ela pode ou não votar. 
idade = int(input("Em que ano você nasceu?\n"))
idade = (2024 - idade)
print(f"Você tem {idade} anos, então: ")
if idade >= 16:
  print("Você pode votar nas próximas eleições!")
else:
  print("Você ainda não pode votar nas eleições.")
