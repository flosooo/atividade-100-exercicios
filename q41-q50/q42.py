# Questão 42: Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
# qualquer e mostre uma contagem até esse valor:
# Ex: Digite um valor: 35
# Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!

numero = int(input('Digite um número inteiro e positivo: '))
for i in range(1, numero + 1):
    print(i)
print('Acabou!')
