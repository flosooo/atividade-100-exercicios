# Questão 62: Faça um programa usando a estrutura “faça enquanto” que leia a idade de
# várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou
# não continuar a digitar dados. No final, quando o usuário decidir parar, mostre
# na tela:
# a) Quantas idades foram digitadas
# b) Qual é a média entre as idades digitadas
# c) Quantas pessoas tem 21 anos ou mais.

idades = []
mais21 = 0

while True:
  idade = int(input('Digite a idade de uma pessoa: '))
  if idade >= 21:
    mais21 += 1
  idades.append(idade)
  r = input('Deseja continuar? [S/N] ')
  if r == "N":
    break
print('\n' * 3)

print(f'Foram digitadas {len(idades)} idades.'
      f'A média entre as idades é de: {sum(idades)/len(idades):.2f}')
print(f'{mais21} pessoas tem 21 anos ou mais.')
