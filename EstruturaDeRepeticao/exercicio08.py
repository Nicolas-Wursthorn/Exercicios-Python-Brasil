# Faça um programa que leia 5 números e informe a soma e a média dos números.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

soma = n1 + n2 + n3 + n4 + n5
media = soma / 5

print("A soma desses números é {}!".format(soma))
print("A média desses números é {}!".format(media))