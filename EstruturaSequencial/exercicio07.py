# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite o valor do lado do quadrado: "))
area = lado * lado
dobro = area * 2
print("O dobro da área desse quadrado é: {}".format(dobro))