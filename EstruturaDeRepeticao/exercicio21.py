# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um número inteiro: "))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end="")
        tot += 1
    else:
        print('\033[31m', end="")
    print("{} ".format(c), end="")
print("\n\033[mO número {} foi divisível {} vezes".format(num ,tot))
if tot == 2:
    print("Esse número é primo!")
else:
    print("Esse número não é primo")
