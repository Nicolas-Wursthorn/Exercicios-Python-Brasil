# Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))

if n1 == n2:
	print("Os números que você digitou tem o mesmo valor!")
elif n1 > n2:
	print("O maior número que você digitou foi: {}".format(n1))
else:
	print("O maior número que você digitou foi: {}".format(n2))