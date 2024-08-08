# Questão 14: A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva  um programa que pergunte 
# a quantidade de Km percorridos por um carro alugado e a  quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço total a pagar,  sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado. 
dias = int(input("Por quantos dias o carro foi alugado?\n"))
km = float(input("Quantos km foram percorridos?\n"))
print(f"O valor total do alugel de {dias} dias é R$: {(dias * 90) + km * 0.20:.1f}")
