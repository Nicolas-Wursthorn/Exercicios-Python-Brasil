# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = int(input("Digite um número inteiro de 1 a 7: "))

texto = "O dia da semana correspondente ao número é: "

if num == 1:
	print(texto + "Domingo.")
elif num == 2:
	print(texto + "Segunda.")
elif num == 3:
	print(texto + "Terça.")
elif num == 4:
	print(texto + "Quarta.")
elif num == 5:
	print(texto + "Quinta.")
elif num == 6:
	print(texto + "Sexta.")
elif num == 7:
	print(texto + "Sábado.")
else:
	print("Valor inválido.")