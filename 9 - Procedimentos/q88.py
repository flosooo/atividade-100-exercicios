# Questão 88: Crie um programa que melhore o procedimento Gerador() da questão anterior
# para que mostre uma mensagem várias vezes.
# Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:
# +-------=======------+
# Aprendendo Portugol
# Aprendendo Portugol
# Aprendendo Portugol
# Aprendendo Portugol
# +-------=======------+

def gerador(mensagem, repeticoes):
    print(" Menu ".center(26, "="))
    for i in range(repeticoes):
        print(mensagem)
    print("".center(26, "="))


gerador("Aprendendo Portugol", 4)
