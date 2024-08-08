# Questão 44: Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
# incremento, mostrando em seguida todos os valores no intervalo:
# Ex: Digite o primeiro Valor: 3
# Digite o último Valor: 10
# Digite o incremento: 2
# Contagem: 3 5 7 9 Acabou!

valor = int(input('Digite o valor inicial da contagem: '))
valor2 = int(input('Digite o valor final da contagem: '))
incremento = int(input('Digite o incremento da contagem: '))

for i in range(valor, valor2, incremento):
  print(i)
print('Acabou!')
