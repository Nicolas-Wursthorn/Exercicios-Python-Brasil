# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

numero = int(input("Digite um número inteiro entre 1 e 10: "))

# if caso o número não esteja entre 1 e 10.
if numero <= 0 or numero > 10:
    print("Esse número não está dentro de 1 e 10! Tente novamente.")
else:
    for count in range(11):
        print("{} X {} = {}".format(numero, count, numero*(count)))