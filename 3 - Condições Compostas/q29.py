# Questão 29: Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%
nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário do funcionário: '))
anos = int(input('Digite a quantidade de anos que o funcionário trabalha na empresa: '))
if anos < 3:
  print(f'{nome.capitalize()}, aumento de 3% no salário. Novo salário: R${salario * 1.03:.2f}')
elif anos > 10:
  print(f'{nome.capitalize()}, aumento de 20% no salário. Novo salário: R${salario * 1.2:.2f}')
else:
  print(f'{nome.capitalize()}, aumento de 12.5% no salário. Novo salário: R${salario * 1.125:.2f}')
