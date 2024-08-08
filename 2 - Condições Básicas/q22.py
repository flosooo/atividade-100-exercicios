# Questão 22: Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.
from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print(f'Você ainda não tem idade para se alistar. Faltam {format(18 - idade)} anos para o alistamento.')
else:
    print(f'Você já passou do tempo de alistamento. Já se passaram {format(idade - 18)} anos do alistamento.')
