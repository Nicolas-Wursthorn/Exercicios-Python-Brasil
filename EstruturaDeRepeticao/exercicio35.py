# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

while True:
    numero = int(input("Montar a tabuado do: "))
    comecar = int(input("Começar por: "))
    terminar = int(input("Terminar em: "))
    if comecar > terminar:
        print("O valor de início é maior que o de término. Tente novamente.")
    else:
        print("Vou montar a tabuado do {} começando em {} e terminando em {}!".format(numero,comecar,terminar))
        for i in range(comecar, terminar + 1):
            print("{} X {} = {}".format(numero, i, i*numero))