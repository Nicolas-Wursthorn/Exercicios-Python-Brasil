# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
	# a. o produto do dobro do primeiro com a metade do segundo.
	# b. a soma do triplo do primeiro com o terceiro.
	# c. o terceiro elevado ao cubo
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite mais um número inteiro: "))
numero3 = float(input("Agora digite um número real: "))

a = (numero1 * 2) * (numero2 / 2)
b = (numero1 * 3) + numero3
c = (numero3 ** 3)

print("O produto do dobro do primeiro com a metade do segundo é: {}".format(a))
print("A soma do triplo do primeiro com a metade do segundo é: {}".format(b))
print("O terceiro elevado ao cubo é: {}".format(c))
