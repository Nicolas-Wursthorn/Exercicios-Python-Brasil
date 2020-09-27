# Faça um programa que leia 5 números e informe o maior número.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

lista = [n1, n2, n3, n4, n5]

print("O maior número é: ", max(lista))
