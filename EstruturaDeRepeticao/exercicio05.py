# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacao_a = int(input("Informe o número da população do país A: "))
populacao_b = int(input("Informe o número da população do país B: "))
taxa_a = float(input("Informe a taxa de crescimento do país A: "))
taxa_b = float(input("Informe a taxa de crescimento do país B: "))
ano = 0

while populacao_a <= populacao_b:
    populacao_a += (populacao_a * taxa_a) / 100
    populacao_b += (populacao_b * taxa_b) / 100
    ano += 1

print("O número necessário de anos para que a população da cidade A ultrapasse a cidade B é de {}".format(ano))