# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
condition = True
while condition:
    numero = int(input("Fatorial de: "))
    resultado=1
    count=1

    if numero > 0 and numero < 16:
        while count <= numero:
            resultado *= count
            count += 1
    else:
        resultado = "O número precisa ser positivo e menor que 16!"
    
    print(resultado)

    