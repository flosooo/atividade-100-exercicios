# Questão 45: O programa acima vai ter um problema quando digitarmos o primeiro valor
# maior que o último. Resolva esse problema com um código que funcione em qualquer situação.

valor = int(input('Digite o valor inicial da contagem: '))
valor2 = int(input('Digite o valor final da contagem: '))
incremento = int(input('Digite o incremento da contagem: '))

if (valor < valor2 and incremento < 0) or (valor > valor2 and incremento > 0):
  incremento = -incremento

for i in range(valor, valor2, incremento):
  print(i)
print('Acabou!')

