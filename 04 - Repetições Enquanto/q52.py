# Questão 52: Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

idades = []
for i in range(10):
  idade = int(input(f"Digite a idade da pessoa {i+1}: "))
  idades.append(idade)

media = sum(idades) / len(idades)
maiores_de_18 = sum(1 for idade in idades if idade > 18)
menores_de_5 = sum(1 for idade in idades if idade < 5)
maior_idade = max(idades)

print(f'\nMédia de idade do grupo:{media},\n'
      f'Pessoas com mais de 18 anos: {maiores_de_18},\n'
      f'Pessoas com menos de 5 anos: {menores_de_5},\n'
      f'Maior idade lida: {maior_idade}')