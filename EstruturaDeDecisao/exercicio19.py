# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#       326 = 3 centenas, 2 dezenas e 6 unidades
#       12 = 1 dezena e 2 unidades 
#       Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = str(input("Digite um número inteiro menor que 1000: "))

if len(num) >= 4:
    print("Número inválido!")
else:
    if len(num) == 1:
        unidade = num[0:2]
        num = int(num)
        if unidade == "1":
            print("1 = 1 unidade.")
        else:
            print("{} = {} unidades.".format(num, unidade))
    elif len(num) == 2:
        dezena = num[0:1]
        unidade = num[1:3]
        num = int(num)
        if dezena == "1" and unidade == "1" :
            print("{} = 1 dezena e 1 unidade.".format(num))
        elif dezena == "1":
            print("{} = 1 dezena e {} unidades.".format(num, unidade))
        elif unidade == "1":
            print("{} = {} dezenas e 1 unidade.".format(num, dezena))
        else:
            print("{} = {} dezenas e {} unidades.".format(num, dezena, unidade))
    elif len(num) == 3:
        centena = num[0:1]
        dezena =  num [1:2]
        unidade = num [2:3]
        num = int(num)
        if centena == "1" and dezena == "1" and unidade == "1":
            print("{} = 1 centena, 1 dezena e 1 unidade.".format(num))
        elif centena == "1" and dezena == "1":
             print("{} = 1 centena, 1 dezenas e {} unidades.".format(num, unidade))
        elif centena == "1" and unidade == "1":
            print("{} = 1 centena, {} dezenas e 1 unidade.".format(num, dezena))
        elif dezena == "1" and unidade == "1":
            print("{} = {} centenas, 1 dezena e 1 unidade.".format(num, centena))
        elif centena == "1":
            print("{} = 1 centena, {} dezenas e {} unidades.".format(num, dezena, unidade))
        elif dezena == "1":
            print("{} = {} centenas, 1 dezena e {} unidades.".format(num, centena, unidade))
        elif unidade == "1":
            print("{} = {} centenas, {} dezenas e 1 unidade.".format(num, centena, dezena))    
        else:
            print("{} = {} centenas, {} dezenas e {} unidades.".format(num, centena, dezena, unidade))


