# Questão 97: Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma
# adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o
# maior entre eles.

def maior(num1, num2, num3):
    numeros = [num1, num2, num3]
    return max(numeros)


a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
print(maior(a, b, c))