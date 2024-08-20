# Questão 77: Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No
# final, mostre uma listagem com todos os nomes informados, na ordem inversa
# daquela em que eles foram informados.
vetorNomes = []
for i in range(7):
  nome = input(f'Digite o {i+1}° nome: ')
  vetorNomes.append(nome)
vetorNomes.reverse()
# ou
# for i in range(6, -1, -1):
#  print(vetorNomes[i])
indices = list(range(len(vetor)))
print(vetor)
print(indices)