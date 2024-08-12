# Melhore o exercício 96, criando além da função Media() uma outra função
# chamada Situacao(), que vai retornar para o programa principal se o aluno está
# APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como
# parâmetro o resultado retornado pela função Media().

def situacao(media):
    if media >= 7:
        print("Aprovado!")
    elif media >= 5:
        print("Recuperação..!")
    else:
        print("Reprovado!")


def media(nota1, nota2):
   return (nota1+nota2)/2


n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))

print(media(n1, n2))

situacao_parametro = media(n1, n2)
situacao(situacao_parametro)
