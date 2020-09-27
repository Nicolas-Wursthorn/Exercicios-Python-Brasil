# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
condition = True
conjunto = []

while condition:
    numero = int(input("Digite os números do conjunto (Digite 0 para parar): "))

    if numero == 0:
        break
    else:
        conjunto.append(numero)

print("Soma dos valores do conjunto: {}!".format(sum(conjunto)))
print("O maior valor do conjunto: {}!".format(max(conjunto)))
print("O menor valor do conjunto: {}!".format(min(conjunto)))

