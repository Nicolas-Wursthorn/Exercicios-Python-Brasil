# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input("Digite um número: "))
div = []
count = 0

for i in range(numero):
    if numero % (i+1) == 0:
        count += 1
        div.append(i+1)

div = str(div).strip("[]")

if count == 2:
    print("Esse número é primo divisível por", div)
else:
    print("Esse número não é primo, divisível por", div)