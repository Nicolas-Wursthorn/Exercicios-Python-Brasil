# Faça um programa que calcule o mostre a média aritmética de N notas.

notas = []
while True:
    nota = float(input("Digite o valor da nota (caso queira parar tecle 0): "))
    notas.append(nota)

    if nota == float(0):
        notas.pop()
        break

media = sum(notas) / len(notas)

print("A média aritmética de todas as notas digitadas é: {}".format(media))


    