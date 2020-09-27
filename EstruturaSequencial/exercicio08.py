# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
porHr = float(input("Quanto você ganha por hora?: "))
hrPMes = int(input("Quantas horas você trabalha no mês?: "))
salario = porHr * hrPMes
print("O total do seu salário no referido mês é: {}".format(salario))
