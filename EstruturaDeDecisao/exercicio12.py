#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#            Salário Bruto: (5 * 220)        : R$ 1100,00
#            (-) IR (5%)                     : R$   55,00  
#            (-) INSS ( 10%)                 : R$  110,00
#            FGTS (11%)                      : R$  121,00
#            Total de descontos              : R$  165,00
#            Salário Liquido                 : R$  935,00

valorHora = float(input("Digite o valor da sua hora: R$"))
qtdHora = int(input("Quantas horas você trabalha por mês?: "))
erro = 0
salarioBruto = (valorHora * qtdHora)

if salarioBruto > 0 and salarioBruto <= 900:
    percentual = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    percentual = 5
elif salarioBruto > 1500 and salarioBruto <= 2500:
    percentual = 10
elif salarioBruto > 2500:
    percentual = 20

IR = (salarioBruto * percentual) / 100
INSS = salarioBruto * 0.1
FGTS = salarioBruto * 0.11
descontos = IR + INSS
salarioLiquido = (salarioBruto - descontos)

print("")
print("Salário Bruto: ({} * {})  : R$ {}".format(qtdHora, valorHora, salarioBruto))
print("(-) IR ({}%)                 : R$ {}".format(percentual, IR))
print("(-) INSS ( 10%)             : R$ {}".format(INSS))
print("FGTS (11%)                  : R$ {}".format(FGTS))
print("Total de descontos          : R$ {}".format(descontos))
print("Salário Líquido             : R$ {}".format(salarioLiquido))
print("")
