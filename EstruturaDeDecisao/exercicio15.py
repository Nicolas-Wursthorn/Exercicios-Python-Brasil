# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#    Dicas:
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))

if lado1 <= lado2 + lado3 and lado2 <= lado1 + lado3 and lado3 <= lado1 + lado2:
	if lado1 == lado2 == lado3:
		print("Triângulo Equilátero.")
	elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
		print("Triângulo Isósceles.")
	else:
		print("Triângulo Escaleno.")
else:
	print("Infelizmente com essas medidas é impossível a existência de um triângulo.")