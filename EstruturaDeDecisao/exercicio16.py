# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
import sys

print("============================================")
print(" Programa de cálculo de equações do 2º grau ")
print("============================================")

a = int(input("Informe o valor de a: "))

if a == 0:
	print("Essa equação não é do 2º grau. Fim da execução.")
else:
	b = int(input("Informe o valor de b: "))
	c = int(input("Informe o valor de c: "))

delta = int((b**2) - 4 * a * c)

if delta < 0:
	print("Delta negativo. Essa equação não possui raízes reais.")
elif delta == 0:
	r = math.sqrt(delta)
	x1 = (- b + r) / (2 * a)
	print("Delta igual a zero. Essa equação possui apenas uma raíz, que é: {}".format(x1))
else:
	r = math.sqrt(delta)
	x1 = (- b + r) / (2 * a)
	x2 = (- b - r) / (2 * a)
	print("Delta positivo. Essa equação possui duas raízes, que são: x1 = {} e x2 = {}".format(x1, x2))
