# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
tamanhoM2 = float(input("Qual o tamanho em metros quadradados da área a ser pintada?: "))

if tamanhoM2 % 54 == 0:
	latas = tamanhoM2 / 54
else:
	latas = int(tamanhoM2 / 54) + 1

preco = latas * 80
print("A quantidade de latas que precisam ser compradas são: {}".format(int(latas)))
print("O preço total a ser pago nas latas é de: R${}".format(preco))