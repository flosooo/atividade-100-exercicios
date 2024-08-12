# Questão 95: Refaça o exercício 90, só que agora em forma de função Somador(), que vai
# receber dois parâmetros e vai retornar o resultado da soma entre eles para o
# programa principal.

def somador(num_a, num_b):
    print(num_a + num_b)


print("="*15, "Somador", "="*15)
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
somador(a, b)