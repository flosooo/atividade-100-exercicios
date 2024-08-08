# Questão 25: Crie um programa que leia o tamanho de três segmentos de reta.
# Analise seus comprimentos e diga se é possível formar um triângulo com essas
# retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
# de cada lado deve ser menor que a soma dos outros dois.

segmento1 = float(input('Digite o comprimento do primeiro segmento: '))
segmento2 = float(input('Digite o comprimento do segundo segmento: '))
segmento3 = float(input('Digite o comprimento do terceiro segmento: '))
if (segmento1 < segmento2 + segmento3 and 
  segmento2 < segmento1 + segmento3 and 
  segmento3 < segmento1 + segmento2):
  print(f'Os segmentos {segmento1}, {segmento2} e {segmento3} podem formar um triângulo')
else: 
  print('Os segmentos não podem formar um triângulo.')
