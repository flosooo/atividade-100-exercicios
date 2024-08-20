# Questão 83: Crie uma lógica que preencha um vetor de 20 posições com números
# aleatórios (entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os
# números gerados e depois coloque o vetor em ordem crescente, mostrando no final
# os valores ordenados.

from random import randint

numeros_aleatorios = [randint(0, 99) for x in range(0, 20)]

numeros_ordenados = sorted(numeros_aleatorios)

print(f"Números gerados: {numeros_aleatorios},\n"
      f"Números colocados em ordem crescente: {numeros_ordenados}.")