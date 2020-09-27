# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros , que custam R$80,00 ou galões de 3,6 litros, que custam R$25,00.
	# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
		# 1. comprar apenas latas de 18 litros;
		# 2. comprar apenas galões de 3,6 litros;
		# 3. misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanhoM2 = float(input("Qual o tamanho em metros quadrados da área a ser pintada?: "))

if tamanhoM2 % 108 == 0:
	latas = tamanhoM2 / 108
else:
	latas = int(tamanhoM2 / 108) + 1

if tamanhoM2 % 21.6 == 0:
	galoes = tamanhoM2 / 21.6
else:
	galoes = int(tamanhoM2 / 21.6) + 1

precoLata = latas * 80
precoGalao = galoes * 25

print("Comprando apenas latas de 18 litros o valor gasto será: R${}".format(precoLata))
print("Comprando apenas galões de 3,6 litros o valor gasto será: R${}".format(precoGalao))
# print("Misturando latas e galões o valor gasto ficaria menor, sendo: R${}".format())
