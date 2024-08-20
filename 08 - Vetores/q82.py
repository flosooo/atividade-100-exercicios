# Questão: 82) Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em
# um vetor. No final, mostre:
# a) Qual é a média da turma
# b) Quantos alunos estão acima da média da turma
# c) Qual foi a maior nota digitada
# d) Em que posições a maior nota aparece


nota_alunos = []
for i in range(5):
    nota = int(input(f'Digite sua nota {i+1}: '))
    nota_alunos.append(nota)

media = sum(nota_alunos) / len(nota_alunos)
print(f"A média da nota das pessoas cadastradas é: {media:.2f}.")

acima_da_media = sum(1 for nota in nota_alunos if nota > media)
print(f"A quantidade de alunos com nota maior que a média são: {acima_da_media}.")

maior_nota = max(nota_alunos)
print(f"A maior nota cadastrada foi: {maior_nota}.")

posicao_maior_nota = [i for i, nota in enumerate(nota_alunos) if nota == maior_nota]
print(f"Posições com a maior nota: {posicao_maior_nota}")
