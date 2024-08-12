# Questão 96: Crie um programa que tenha uma função Media(), que vai receber as 2 notas de
# um aluno e retornar a sua média para o programa principal.

def media(nota1, nota2):
    print((nota1+nota2)/2)


n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media(n1,n2)