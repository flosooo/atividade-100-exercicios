# Questão 94: [DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado
# Fibonacci() que recebe um único valor inteiro como parâmetro, indicando quantos
# termos da sequência serão mostrados na tela. O seu procedimento deve receber
# esse valor e mostrar a quantidade de elementos solicitados.
# Obs: Use os exercícios 70 e 75 para te ajudar na solução
# Ex:
# Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM
# Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >>

def fibonacci(n):
    if n <= 0:
        print("Por favor, insira um número inteiro positivo.")
        return
    a, b = 1, 1
    sequencia_fibonacci = []

    for i in range(n):
        sequencia_fibonacci.append(a)
        a, b = b, a + b
    print("Sequência de Fibonacci:")
    print(sequencia_fibonacci)


fibonacci(int(input("Deseja ir até que termo da sequência de Fibonacci? ")))