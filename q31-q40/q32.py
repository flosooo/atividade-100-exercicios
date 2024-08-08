# Questão 32: Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
# jogador vai tentar descobrir qual foi o valor sorteado.
import random

while True:
    escolha = int(input('O computador vai sortear números de 1 a 5. Tente adivinhar qual foi o número sorteado: \n'))

    while escolha < 1 or escolha > 5:
        escolha = int(input('Número inválido, tente novamente!\nDigite um número entre 1 e 5: \n'))

    sorteio = random.randint(1, 5)

    if escolha == sorteio:
        print(f'Parabéns, você acertou! O número sorteado foi {sorteio}.')
        break
    else:
        print(f'Você errou, o número sorteado foi {sorteio}. \nTente novamente!')
