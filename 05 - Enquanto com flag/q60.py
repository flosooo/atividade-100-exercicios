# Questão 60: Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
# O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos


nome_pessoa_mais_velha = ''
maior_idade = -1
nome_mulher_mais_jovem = ''
idade_mulher_jovem = float('inf')

total_idade = 0
pessoas = 0
homem_maior_30 = 0
mulheres_menores_18 = 0

while True:
    print("="*30)
    nome = str(input('Nome: '))
    idade = int(input('idade: '))
    sexo = input("Sexo:\n"
                 "1 = Masculino.\n"
                 "2 = Feminino. ")
    print("="*30)

    # Atualiza a pessoa mais velha:
    if idade > maior_idade:
        maior_idade = idade
        nome_pessoa_mais_velha = nome

    # Caso seja homem:
    if sexo == "1":
        if idade > 30:
            homem_maior_30 += 1
    # Caso seja mulher:
    elif sexo == "2":
        if idade < 18:
            mulheres_menores_18 += 1
        if idade < idade_mulher_jovem:
            idade_mulher_jovem = idade
            nome_mulher_mais_jovem = nome
    else:
        print("Valor inválido, use 1 ou 2 para escolher entre homem e mulher.")
        continue

    total_idade = total_idade + idade
    pessoas += 1

    continuar = input("Quer continuar? [S/N] ").capitalize().strip()[0]
    if continuar != "S":
        break

media = total_idade / pessoas if pessoas > 0 else 0

print("="*30)
print(f"Nome da pessoa mais velha é: {nome_pessoa_mais_velha},\n"
      f"Nome da mulher mais jovem: {nome_mulher_mais_jovem},\n"
      f"Média da idade do grupo: {media:.2f},\n"
      f"Quantidade de homens com mais de 30 anos: {homem_maior_30},\n"
      f"Quantidade de mulheres com menos de 18 anos: {mulheres_menores_18}.")
print("="*30)
