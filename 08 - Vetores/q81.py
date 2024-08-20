# Questão 81: Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No
# final, mostre:
# a) Qual é a média de idade das pessoas cadastradas
# b) Em quais posições temos pessoas com mais de 25 anos
# c) Qual foi a maior idade digitada (podem haver repetições)
# d) Em que posições digitamos a maior idade

idade_pessoas = []
for i in range(8):
    idade = int(input(f'Digite sua idade {i+1}: '))
    idade_pessoas.append(idade)

media = sum(idade_pessoas) / len(idade_pessoas)
print(f"A média da idade das pessoas cadastradas é: {media:.2f}")

posicao_maior_25 = [i for i, idade in enumerate(idade_pessoas) if idade > 25]
print(f"As posiçoes das pessoas com mais de 25 anos são: {posicao_maior_25}.")

maior_idade = max(idade_pessoas)
print(f"A maior idade cadastrada foi: {maior_idade}.")

posicao_maior_idade = [i for i, idade in enumerate(idade_pessoas) if idade == maior_idade]
print(f"Posição com a maior idade: {posicao_maior_idade}")
