# Questão 16:  Escreva um programa para calcular a redução do tempo de vida de um  fumante. Pergunte a quantidade de cigarros fumados 
# por dias e quantos anos ele  já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. 
# Calcule  quantos dias de vida um fumante perderá e exiba o total em dias. 
anos = int(input("Há quantos anos você fuma?\n"))
cigarros = int(input("Quantos cigarros você fuma por dia?\n"))
dias = anos * 365 * cigarros * 10/1440
print(f"Aproximadamente, você perdeu {dias:.0f} possíveis dias de vida")
