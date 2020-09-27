# Tendo como dado de entrada a altura(h) de uma pessoa, construa um algorítmo que calcule seu peso ideal utilizando as seguintes fórmulas:
	# a. Para homens: (72.7 * h) - 58
	# b. Para mulheres: (62.1 * h) - 44.7
altura = float(input("Digite sua altura em metros: "))
genero = int(input("Digite 1 (um) se você é homem, e 2 (dois) se é mulher: "))

if genero == 1:
	peso = (72.7 * altura) - 58

if genero == 2:
	peso = (62.1 * altura) - 44.7

print("O seu peso ideal baseado na sua altura seria: {}".format(peso))