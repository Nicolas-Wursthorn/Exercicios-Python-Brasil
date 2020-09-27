# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                         Até 5 Kg           Acima de 5 Kg
#   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#   Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = float(input("Digite a quantidade de morangos a ser comprados (em Kg): "))
maca = float(input("Digite a quantidade de maçãs a ser comprados (em Kg): "))

if morango <= 0 or maca <= 0:
    print("Valor em quilos incorreto.")
elif morango <= 5 and maca <= 5:
    valor = (morango * 2.50) + (maca * 1.80)
elif morango > 5 and maca > 5:
    valor = (morango * 2.20) + (maca * 1.50)
elif morango <= 5 and maca > 5:
    valor = (morango * 2.50) + (maca * 1.50)
else:
    valor = (morango * 2.20) + (maca * 1.80)

frutasJuntas = morango + maca

if frutasJuntas > 8 or valor > 25:
    valor = valor - (valor * 0.1)

print("A quantidade de morangos compradas foi {}Kg e de maçãs foi {}Kg, o valor total foi de: R${}".format(morango, maca, round(valor, 2)))
