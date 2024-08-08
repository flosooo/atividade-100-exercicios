# Questão 37: Uma empresa precisa reajustar o salário dos seus funcionários, dando um
# aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
# o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
# No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
# - menos de 15 anos de empresa: +5%
# - de 15 até 20 anos de empresa: +12%
# - mais de 20 anos de empresa: +23%
# - Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%

salario = float(input('Digite o salário atual: '))
genero = input('Digite o gênero do funcionário (M/F): ')
tempo_empresa = int(input('Digite quantos anos o funcionário trabalhou na empresa: '))
if genero == 'M':
  if tempo_empresa < 20:
    salario *= 1.03
  elif tempo_empresa >= 20 and tempo_empresa <= 30:
    salario *= 1.13
  else:
    salario *= 1.25
else: 
  if tempo_empresa < 15:
    salario *= 1.05
  elif tempo_empresa >= 15 and tempo_empresa <= 20:
    salario *= 1.12
  else:
    salario *= 1.23

print(f'O novo salário é R${salario:.2f}')
