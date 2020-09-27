# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
	# a. salário bruto.
	# b. quanto pagou de INSS.
	# c. quanto pagou ao sindicato.
	# d. o salário liquido.

porHr = float(input("Quanto você ganha por hora?: R$"))
hrPMes = float(input("Quantas horas você trabalha por mês?: "))
salario = porHr * hrPMes

IR = salario * 0.11
INSS = salario * 0.08
sindicato = salario * 0.05
liquido = salario - IR - INSS - sindicato
bruto = salario

print("Salário Bruto: R${}".format(bruto))
print("IR (11%): R${}".format(IR))
print("INSS (8%): R${}".format(INSS))
print("Sindicato (5%): R${}".format(sindicato))
print("Salário Liquido: R${}".format(liquido))