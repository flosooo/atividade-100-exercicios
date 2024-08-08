# Questão 54: Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, 
# mostrando no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

dic = {
  'peso':[],
  'altura':[]
}

for i in range(7): 
  dic['altura'].append(float(input(f'Digite a altura da {i+1}° pessoa: ')))
  dic['peso'].append(float(input(f'Digite o peso da {i+1}° pessoa: ')))
  print('\n')

mediaAlt = sum(dic['altura']) / len(dic['altura'])
pesoMaior90 = 0
menos50mais16m = 0
mais100mais19m = 0

for i in dic['peso']:
  if i > 90:
    pesoMaior90 += i
  if i < 50 and dic['altura'][dic['peso'].index(i)] < 1.60:
    menos50mais16m += 1
  if i > 100 and dic['altura'][dic['peso'].index(i)] > 1.90:
    mais100mais19m += 1
print(f'A média de altura do grupo é {mediaAlt:.2f}m\n'
      f'A quantidade de pessoas que pesam mais de 90Kg é {pesoMaior90}\n'
      'A quantidade de pessoas que pesam menos de 50Kg e '
      f'medem mais de 1.60m é {menos50mais16m}\n'
      f'A quantidade de pessoas que pesam mais de 100Kg '
      f'e medem mais de 1.90 é {mais100mais19m}\n')
  