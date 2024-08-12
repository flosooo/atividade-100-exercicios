# Questão 89: Crie um programa que melhore o procedimento Gerador() da questão anterior
# para que o programador possa escolher uma entre três bordas:
# +-------=======------+ Borda 1
# ~~~~~~~~:::::::~~~~~~~ Borda 2
# <<<<<<<<------->>>>>>> Borda 3
# Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)
# ~~~~~~~~:::::::~~~~~~~
# Portugol Studio
# Portugol Studio
# Portugol Studio
# ~~~~~~~~:::::::~~~~~~~

def gerador(mensagem, repeticoes, borda):
    if borda == 1:
        borda = "+-------=======------+"
    elif borda == 2:
        borda = " ~~~~~~~~:::::::~~~~~~~"
    elif borda == 3:
        borda = "<<<<<<<<------->>>>>>>"
    else:
        print("Insira um valor válido.")
    print(borda)
    for i in range(repeticoes):
        print(mensagem)
    print(borda)


print("+-------=======------+ Borda 1 \n"
      "~~~~~~~~:::::::~~~~~~~ Borda 2 \n"
      "<<<<<<<<------->>>>>>> Borda 3")

gerador("Portugol Studio", 3, int(input("Deseja escolher qual borda? ")))
