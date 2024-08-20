# Questão 59: Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
# perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
# a) qual é a maior idade lida
# b) quantos homens foram cadastrados
# c) qual é a idade da mulher mais jovem
# d) qual é a média de idade entre os homens

idade_mulher_jovem = 0
maior_idade = 0
soma_idade_homens = 0
total_homem = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = input("Sexo:\n"
                 "1 = Masculino.\n"
                 "2 = Feminino. ")

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "1":
        total_homem += 1
        soma_idade_homens += idade
    elif sexo == "2":
        if idade_mulher_jovem < idade:
            idade_mulher_jovem = idade
    else:
        print("Valor inválido, use 1 ou 2 para escolher entre homem e mulher.")
        continue

    continuar = input("Quer continuar? [S/N] ").capitalize().strip()[0]
    if continuar != "S":
        break

media_masc = soma_idade_homens / total_homem if total_homem > 0 else 0

print(f"A maior idade lida foi: {maior_idade},\n"
      f"Homens cadastrados: {total_homem},\n"
      f"Idade da mulher mais jovem: {idade_mulher_jovem},\n"
      f"Média da idade masculina: {media_masc}")
