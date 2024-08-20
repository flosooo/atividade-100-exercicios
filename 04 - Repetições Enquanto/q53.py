# Questão 53: Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos
dic = {
  'nomes' :[],
  'idades':[],
  'generos':[]
}

for i in range(5): 
  dic['nomes'].append(input(f'Digite o nome da {i+1}° pessoa: '))
  dic['idades'].append(int(input(f'Digite a idade da {i+1}° pessoa: ')))
  dic['generos'].append(input('Digite o gênero (M/F): '))
  print('\n')

somaM = 0
somaF = 0
soma_idade_homens = 0
mulheres_20_mais = 0

for i in range(len(dic['generos'])):
  if dic['generos'][i] == 'M':
    somaM += 1
    soma_idade_homens += dic['idades'][i]
  else:
    somaF += 1
    if dic['idades'][i] > 20:
      mulheres_20_mais += 1

media_grupo = sum(dic['idades']) / len(dic['idades'])

media_idade_homens = soma_idade_homens / somaM if somaM > 0 else 0

print(f'A quantidade de homens cadastrados é: {somaM}')
print(f'A quantidade de mulheres cadastradas é: {somaF}')
print(f'A média de idade do grupo é {media_grupo:.2f}.')
print(f'A média de idade dos homens é {media_idade_homens:.2f}.')
print(f'A quantidade de mulheres com mais de 20 anos é: {mulheres_20_mais}')