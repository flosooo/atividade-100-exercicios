# Questão 90: Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses
# valores para um procedimento Somador() que vai calcular e mostrar a soma entre
# eles.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))


def somador():
    print("A soma entre os dois números é: ", a + b)


somador()