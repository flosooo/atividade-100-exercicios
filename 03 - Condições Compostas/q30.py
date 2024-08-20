# Questão 30: Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes

segmento1 = float(input('Digite o comprimento do primeiro segmento: '))
segmento2 = float(input('Digite o comprimento do segundo segmento: '))
segmento3 = float(input('Digite o comprimento do terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Os segmentos acima podem formar um triângulo.')
    if segmento1 == segmento2 == segmento3:
        print('O triângulo é equilátero.')
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
