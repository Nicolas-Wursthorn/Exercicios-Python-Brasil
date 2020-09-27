# Faça um programa que leia três números e mostre eles em ordem decrescente.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))
n3 = float(input("Agora mais um número: "))

if n1 > n2 and n1 > n3:
	print("Maior: {}".format(n1))
	if n2 > n3:
		print("Meio: {}".format(n2))
		print("Menor: {}".format(n3))
	else:
		print("Meio: {}".format(n3))
		print("Menor: {}".format(n2))
elif n2 > n1 and n2 > n3:
	print("Maior: {}".format(n2))
	if n1 > n3:
		print("Meio: {}".format(n1))
		print("Menor: {}".format(n3))
	else:
		print("Meio: {}".format(n3))
		print("Menor: {}".format(n1))
elif n3 > n1 and n3 > n2:
	print("Maior: {}".format(n3))
	if n1 > n2:
		print("Meio: {}".format(n1))
		print("Menor: {}".format(n2))
	else:
		print("Meio: {}".format(n2))
		print("Menor: {}".format(n1))



