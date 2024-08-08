# Questão 24: Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
# viagens até 200Km e R$0.45 para viagens mais longas.
distancia = float(input("Digite a distância que deseja percorrer em Km: "))
preco = distancia * 0.45 if distancia > 200 else distancia * 0.5
print(f"O preço da passagem é R${preco:.2f}")
