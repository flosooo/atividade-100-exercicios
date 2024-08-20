# Questão 31: Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
import random

escolha = input('Vamos jogar Jokenpo! Escolha pedra, papel ou tesoura: ').lower()
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)

vencedor = {
  'pedra': 'tesoura',
  'papel': 'pedra',
  'tesoura': 'papel'
  }

if escolha == computador:
  print(f'Empate! O computador escolheu {computador}.')
elif vencedor[escolha] == computador:
  print(f'Você ganhou! O computador escolheu {computador}.')
else:
  print(f'Você perdeu! O computador escolheu {computador}.')
