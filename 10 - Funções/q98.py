# Questão 98: Crie um programa que tenha uma função SuperSomador(), que vai receber dois
# números como parâmetro e depois vai retornar a soma de todos os valores no
# intervalo entre os valores recebidos.
# Ex:
# SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
# SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85

def super_somador(num1, num2):
    soma = 0
    if num1 < num2:
        for num1 in range(num1, num2+1):
            soma = soma + num1
    else:
        for num2 in range(num2, num1+1):
            soma = soma + num2
    print(soma)


a = int(input("Início da super soma: "))
b = int(input("Fim da super soma: "))
super_somador(a, b)