# Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua  média e mostre na tela. No final, 
# analise a média e mostre se o aluno teve ou  não um bom aproveitamento (se ficou acima da média 7.0). 
nome = input("Qual o seu nome?\n")
nota1 = float(input("Qual a sua primeira nota?\n"))
nota2 = float(input("Qual a sua segunda nota?\n"))
media = (nota1 + nota2) / 2
print(f"{nome}, sua média é: {media}")

if media >= 7:
  print("Parabéns, você foi aprovado!")
else:
  print("Você infelizmente não atingiu a média.")
