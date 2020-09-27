# # Altere o programa anterior para mostrar no final a soma dos números.

# n1 = int(input("Digite um número inteiro: "))
# n2 = int(input("Digite um número inteiro: "))

# while n1 > n2:
#     n1 = int(input("Digite um número inteiro (O primeiro número deve ser o maior): "))
#     n2 = int(input("Digite um número inteiro: "))  

# for n in range(n1, n2, 1):
#     print(n)

# print("Soma dos números: ", n + n)

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

for i in range(n1 + 1, n2):
        print(i)

for i in range(n2 + 1, n1):
        print(i)

print("Soma dos números: ", i + i)