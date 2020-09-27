# Faça um programa que leia três números e mostre o maior deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))
n3 = float(input("Agora mais um número: "))

if n1 > n2:
	print("O maior número que você digitou foi: {}".format(n1))
elif n2 > n1:
	print("O maior número que você digitou foi: {}".format(n2))
else:
	print("O maior número que você digitou foi: {}".format(n3))	
