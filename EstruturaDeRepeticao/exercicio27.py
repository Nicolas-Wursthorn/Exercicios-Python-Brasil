# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cds = int(input("Digite e quantidade de CD's da sua coleção: "))
valores = []
count = 0

while count < cds:
    valor = float(input("Digite o valor do CD {}: ".format(count+1)))
    valores.append(valor)
    count += 1

total = sum(valores)
media = total / cds

print("O valor total investido na coleção foi de R${}, e o valor médio por CD R${}!".format(total, media))