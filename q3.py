# Questão 3: Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.

funcionario_nome = input("Qual é o seu nome? ")
funcionario_salario = float(input("Informe o seu salário: "))
print(f"Nome do funcionário: {funcionario_nome}"
      f"\nSalário: {funcionario_salario}"
      f"\nO funcionário {funcionario_nome} tem um salário de R${funcionario_salario} em Junho.")
