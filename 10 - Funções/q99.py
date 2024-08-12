# Faça um programa que possua uma função chamada Potencia(), que vai receber
# dois parâmetros numéricos (base e expoente) e vai calcular o resultado da
# exponenciação.
# Ex: Potencia(5,2) vai calcular 5
# 2 = 25

def potencia(num1, num2):
    return num1 ** num2


a = int(input("Base da potenciação: "))
b = int(input("Expoente: "))
print(potencia(a, b))