# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from datetime import date

print("====================")
print(" VALIDADOR DE DATAS ")
print("====================")

data = str(input("Digite uma data (dd/mm/aaaa): "))
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

validade = "true"
i = 0

while validade == "true" and i == 0:
    if ano % 4 == 0:
        bissexto = "true"
    else:
        bissexto =  "false"

    if mes < 1 or mes > 12:
        validade = "false"

    if dia > 31 or ((mes == 4 or mes == 6 or mes == 8 or mes == 9 or mes == 11) and dia > 30):
        validade = "false"

    if (mes == 2 and bissexto == "false" and dia > 28) or (mes == 2 and bissexto == "true" and dia < 29):
        validade = "false"
    
    i = i + 1

if validade == "true":
    print("Data válida")
else:
    print("Data inválida")