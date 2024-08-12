# Questão 87: Crie um programa que melhore o procedimento Gerador() da questão anterior
# para que mostre uma mensagem personalizada, passada como parâmetro. Ex: Ao
# chamar Gerador("Aprendendo Portugol") aparece:
# +-------=======------+
# Aprendendo Portugol
# +-------=======------+

def gerador(mensagem):
    print(" Menu ".center(26, "="))
    print(mensagem)
    print("".center(26, "="))


gerador(input("Mensagem que deseja gerar: "))
