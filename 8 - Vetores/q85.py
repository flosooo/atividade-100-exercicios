# Questão 85: Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários e
# guarde esses dados em três vetores. No final, mostre uma listagem contendo
# apenas os dados das funcionárias mulheres que ganham mais de R$5 mil.

nomes = []
sexos = []
salarios = []

for i in range(2):
    print("="*30)
    nome_input = str(input('Nome: '))
    nomes.append(nome_input)
    sexo_input = str(input('Sexo [M/F]: ')).capitalize().strip()[0]
    sexos.append(sexo_input)
    salario_input = float(input('Salário: '))
    salarios.append(salario_input)

print("\nFuncionárias mulheres que ganham mais de R$5.000,00:")
for i in range(2):
    if sexos[i] == 'F' and salarios[i] > 5000:
        print(f"Nome: {nomes[i]}, Salário: {salarios[i]}")
