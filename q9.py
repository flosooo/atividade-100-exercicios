# Questão 9: Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

dinheiro_em_reais = float(input("Informe o dinheiro em reais: "))
print(f"Você pode comprar ${dinheiro_em_reais * 3.45}")
