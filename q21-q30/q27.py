# Questão 27: Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
notas = []
for i in range(2):
    while True:
        nota = float(input(f'Digite a nota {i+1} (entre 0 e 10): '))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida! Por favor, insira um valor entre 0 e 10.")

nota1, nota2 = notas[0], notas[1]

media = sum(notas) / notas.__len__()
print(f'Sua média é: {media}')

if media < 5:
  print('De acordo com a média, você está REPROVADO')
elif media >= 5 and media < 7:
  print('De acordo com a média, você têm direito a RECUPERAÇÃO')
else: 
  print('De acordo com a média, você está APROVADO')
