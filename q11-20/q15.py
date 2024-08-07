# Questão 15: Crie um programa que leia o número de dias trabalhados em um mês e mostre o  salário de um funcionário, 
# sabendo que ele trabalha 8 horas por dia e ganha R$25  por hora trabalhada. 
dias = int(input("Quantos dias foram trabalhados no mês?\n"))
print(f"O salário para {dias} dias trabalhados é de R$: {(dias * 8 * 25)}")
