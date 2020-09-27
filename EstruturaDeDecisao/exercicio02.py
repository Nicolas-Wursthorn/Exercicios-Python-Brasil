# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = float(input("Digite um valor: "))

if valor == 0:
	print("Esse valor é nulo!")
elif valor > 0:
	print("Esse valor é positivo!")
else:
	print("Esse valor é negativo!")