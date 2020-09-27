# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

count = 1
pares = []
impares = []

while count <= 10:
    num = int(input("Digite um número: "))
    count += 1
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares = str(pares).strip('[]')
impares = str(impares).strip('[]')

print("Numeros pares: {}.".format(pares))
print("Numeros ímpares: {}.".format(impares))
