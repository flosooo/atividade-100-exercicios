# Questão 86: Crie um programa que tenha um procedimento Gerador() que, quando chamado,
# mostre a mensagem "Olá, Mundo!" com algum componente visual (linhas) Ex: Ao
# chamar Gerador() aparece:
# +-------=======------+
# Olá, Mundo!
# +-------=======------+

def gerador():
    print(" Menu ".center(26, "#"))
    print("Olá, Mundo!")
    print("".center(26,"#"))


gerador()
