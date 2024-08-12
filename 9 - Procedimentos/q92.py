# Questão 92: Crie uma lógica que leia um número inteiro e passe para um
# procedimento ParOuImpar() que vai verificar e mostrar na tela se o valor
# passado como parâmetro é PAR ou ÍMPAR.

def par_ou_impar(numero):
    if numero % 2 == 0:
        print('Par')
    else:
        print('Impar')


par_ou_impar(int(input("Insira um número: ")))

