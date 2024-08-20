# Questão 68: Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura
# “para”. No final, mostre na tela:
# a) Quantas mulheres foram cadastradas
# b) Quantos homens pesam mais de 100Kg
# c) A média de peso entre as mulheres
# d) O maior peso entre os homens

homens = []
mulheres = []
mais100 = 0
for i in range(8):
  sexo = input(f'Digite o sexo [M/F] {i+1}° pessoa: ')
  peso = float(input(f'Digite o peso da {i+1} pessoa: '))
  if sexo == 'M':
    homens.append(peso)
    if peso > 100:
      mais100+=1
  else:
    mulheres.append(peso)
    
print(f'Foram cadastradas {len(mulheres)} mulheres')
print(f'Homens que pesam mais de 100Kg:{mais100} ')
print('A média de peso entre as mulheres é:'                   
      f'{sum(mulheres)/len(mulheres):.2f}')
print(f'O maior peso entre os homens é: {max(homens)}')