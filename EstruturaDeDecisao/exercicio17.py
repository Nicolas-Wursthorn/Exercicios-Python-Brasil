# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
from datetime import date

print("=============================")
print(" VERIFICADOR DE ANO BISSEXTO ")
print("=============================")

ano_atual = date.today()
ano = int(input("Digite um ano que desekja verificar: "))

if ano > ano_atual.year:
    print("Opa, ano inválido.")
elif ano % 4 == 0:
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto.")