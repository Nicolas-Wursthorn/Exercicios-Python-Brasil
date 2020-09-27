# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro. 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = float(input("Digite o valor de litros comprados: "))
combustivel = input("Qual o tipo do combustível? (A-álcool G-gasolina): ")

if litros <= 0 or combustivel != "A" or combustivel != "G":
    print("Falha no cálculo do valor. Verifique se as informações foram inseridas corretamente.")
elif litros <= 20 and combustivel == "A":
    valor = litros * 1.84 # desconto de 3% já aplicado.
    print("O preço a ser pago pelo combustível de tipo A-álcool é: R${}".format(round(valor, 2)))
elif litros > 20 and combustivel == "A":
    valor = litros * 1.80 # desconto de 5% já aplicado.
    print("O preço a ser pago pelo combustível de tipo A-álcool é: R${}".format(round(valor, 2)))
elif litros <= 20 and combustivel == "G":
    valor = litros * 2.40 # desconto de 4% já aplicado.
    print("O preço a ser pago pelo combustível de tipo G-gasolina é: R${}".format(round(valor,2)))
elif litros > 20 and combustivel == "G":
    valor = litros * 2.35 # desconto de 6% já aplicado.
    print("O preço a ser pago pelo combustível de tipo G-gasolina é: R${}".format(round(valor,2)))