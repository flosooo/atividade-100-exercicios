# Questão 91: Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses
# valores para um procedimento Maior() que vai verificar qual deles é o maior e
# mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem
# informando essa característica.

def maior(num1, num2):
    if num1 > num2:
        print(f"{num1} é maior que {num2}")
    elif num2 > num1:
        print(f"{num2} é maior que {num1}")
    else:
        print("Os números são iguais.")


maior(float(input("Primeiro número: ")), float(input("Segundo número: ")))