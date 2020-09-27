# Faça um programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))
n3 = float(input("Agora mais um número: "))

menor = n1

if n2 < n1 and n2 < n3:
	menor = n2
elif n3 < n1 and n3 < n2:
	menor = n3

print("O menor valor digitado foi {}".format(menor))

maior = n1

if n2 > n1 and n2 > n3:
	maior = n2
elif n3 > n1 and n3 > n2:
	maior = n3

print("O maior valor digitado foi {}".format(maior))