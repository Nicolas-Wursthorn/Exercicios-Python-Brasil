# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite o primeiro número: "))
expoente = int(input("Digite o segundo número: "))
count = 1
potencia = 1

while count <= expoente:
    potencia = potencia * base
    count += 1

print("O primeiro número elevado ao segundo número é igual a: {}".format(potencia))