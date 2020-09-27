# Tendo como dados de entrada a altura de uma pessoa, construa um algorítmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Digite sua altura em metros: "))
peso = (72.7 * altura) - 58
print("O seu peso ideal baseado na sua altura é: {}kg".format(peso))