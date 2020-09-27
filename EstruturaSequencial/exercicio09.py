# Faça um programa que peça a temperatura em graus Farenheit, transforme e mostre em graus Celsius.
farenheit = float(input("Digite a temperatura em Farenheit: "))
celsius = (5 * (farenheit - 32) / 9)
print("A temperatura que você digitou, em graus Celsius é: {}".format(celsius))