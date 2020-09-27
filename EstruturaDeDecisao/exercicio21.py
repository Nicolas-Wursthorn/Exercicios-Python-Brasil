# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#   Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#   Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = float(input("Qual o valor desejado para o saque?: "))

if saque < 10:
    print("Desculpe, o valor mínimo de saque é R$10,00.")
elif saque > 600:
    print("Desculpe, o valor máximo de saque é R$600,00")
else:

    valorTotal = saque

    notas100 = saque//100
    saque -= (notas100 * 100)

    notas50 = saque//50
    saque -= (notas50 * 50)

    notas10 = saque//10
    saque -= (notas10 * 10)

    notas5 = saque//5
    saque -= (notas5 * 5)

    notas1 = saque//1

    print("Para sacar R${}, foram necessárias {} notas de cem, {} notas de 50, {} notas de 10, {} notas de 5 e {} notas de 1.".format(valorTotal, notas100, notas50, notas10, notas5, notas1))