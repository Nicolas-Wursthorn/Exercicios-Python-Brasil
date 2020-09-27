# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))

while n1 > n2:
    n1 = int(input("Digite um número inteiro (O primeiro número deve ser o maior): "))
    n2 = int(input("Digite um número inteiro: "))  

for n in range(n1, n2, 1):
    print(n)