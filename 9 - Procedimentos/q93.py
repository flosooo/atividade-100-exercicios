# Questão 93: Faça um programa que tenha um procedimento chamado Contador() que recebe
# três valores como parâmetro: o início, o fim e o incremento de uma contagem.
# O programa principal deve solicitar a digitação desses valores e passá-los ao
# procedimento, que vai mostrar a contagem na tela.

def contador(inicio, fim, incremento):
    for numero in range(inicio, fim, incremento):
        print(numero)


contador(int(input("Inicio da contagem: ")), int(input("Fim da contagem: ")), int(input("Pulará quantos caracteres: ")))
