# Questão 55: Vamos melhorar o jogo que fizemos no exercício 32. A partir de
# agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4
# tentativas para tentar acertar.

# "Questão 32: Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
# jogador vai tentar descobrir qual foi o valor sorteado."
import random

sorteio = random.randint(1, 10)
tentativas = 4

while tentativas > 0:
  escolha = int(input(f'Você tem {tentativas} tentativa(s). Tente adivinhar o número ' 
                      'sorteado (entre 1 e 10): \n'))


  while escolha < 1 or escolha > 10:
      escolha = int(input('Número inválido! Digite um número entre 1 e 10: \n'))


  if escolha == sorteio:
      print('Parabéns! Você acertou!')
      break  
  else:
      tentativas -= 1 
      if tentativas > 0:
          print('Tente novamente!\n')
      else:
          print(f'Que pena! Você não acertou. O número sorteado foi {sorteio}.')

print('Fim do jogo. Obrigado por jogar!')