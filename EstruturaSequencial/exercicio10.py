# Faça um programa que peça a temperatura em graus Celsius e mostre em graus Farenheit.
celsius = float(input("Digite a temperatura em graus Celsius: "))
farenheit = (celsius * 9/5) + 32
print("A temperatura que você digitou, em Farenheit é: {}".format(farenheit))