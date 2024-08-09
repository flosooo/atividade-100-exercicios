# Questão 56: Crie um programa que leia vários números pelo teclado e mostre no final o
# somatório entre eles.
# Obs: O programa será interrompido quando o número 1111 for digitado

numero = 0
somatorio = 0
while numero != 1111:
    numero = int(input("Digite seus números: "))
    somatorio += numero

print(somatorio)