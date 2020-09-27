# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                              Até 5 Kg           Acima de 5 Kg
#        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("="*36)
print(" BEM-VINDO AO HIPERMERCADO TABAJARA ")
print("="*36)

tipoCarne = input("Qual o tipo de carne comprada? F-file duplo A-alcatra P-picanha: ").upper()
qtdCarne = float(input("Qual a quantidade de carne comprada? (em Kg): "))
tipoPagamento = input("A compra foi feita no cartão Tabajara?: [S ou N]: ").upper()


print("============= CUPOM FISCAL =============")    

if tipoCarne == "F":
    print("|| Carne escolhida : File Duplo       ||")
    if qtdCarne <= 5:
        valorBruto = qtdCarne * 4.90
    else:
        valorBruto = qtdCarne * 5.80

elif tipoCarne == "A":
    print("|| Carne escolhida : Alcatra          ||")
    if qtdCarne <=5:
        valorBruto = qtdCarne * 5.90
    else:
        valorBruto = qtdCarne * 6.80

else:
    print("|| Carne escolhida : Picanha          ||")
    if qtdCarne <= 5:
        valorBruto = qtdCarne * 6.90
    else:
        valorBruto = qtdCarne * 7.80

print("|| Quantidade : {}Kg                 ||".format(qtdCarne))

desconto = 0.0
if tipoPagamento == "S":
    print("|| Pagamento com cartão TABAJARA      ||")
    desconto = valorBruto * 0.05
else:
    print("|| Pagamento sem cartão TABAJARA      ||")

print("|| Valor : {}                       ||".format(round(valorBruto,2)))
print("|| Desconto : R${}                  ||".format(round(desconto,2)))
print("|| Valor total: R${}               ||".format(round((valorBruto - desconto),2)))
print("========================================")

