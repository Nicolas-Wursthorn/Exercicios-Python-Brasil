# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000

condition = True
conjunto = []

while condition:
    numero = int(input("Digite os números do conjunto (Digite 0 para parar): "))

    if numero == 0:
        break
    elif numero > 1000 or numero < 0:
        print("Digite somente números entre 0 e 1000.")
    else:
        conjunto.append(numero)
        

print("Soma dos valores do conjunto: {}!".format(sum(conjunto)))
print("O maior valor do conjunto: {}!".format(max(conjunto)))
print("O menor valor do conjunto: {}!".format(min(conjunto)))