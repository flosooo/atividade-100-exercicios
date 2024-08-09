# Questão 57: Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
# No final, mostre o total de salários pagos aos homens e o total pago às
# mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
# sempre que ler os dados de um funcionário.


salarios = [0, 0]
homens = 0
mulheres = 0

while True:
    salario = float(input("Qual o seu salário? "))
    sexo = int(input("Qual o seu sexo?\n"
                     "1 = Masculino\n"
                     "2 = Feminino "))
    if sexo == 1:
        homens += 1
        salarios[0] += salario
    elif sexo == 2:
        mulheres += 1
        salarios[1] += salario
    else:
        print("Informação inválida.")
        break

    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break

print(f"Total de homens: {homens}\n"
      f"Total de mulheres: {mulheres}\n"
      f"Total do salário dos homens: {salarios[0]}, total do salário das mulheres: {salarios[1]}.")
