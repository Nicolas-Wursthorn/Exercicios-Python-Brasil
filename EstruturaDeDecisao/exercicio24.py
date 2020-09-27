# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação deseja realizar entre os dois números (+ , - , / , * ): ")

if operacao == "+":
    resultado = num1 + num2
    # PAR OU ÍMPAR
    if resultado == 0:
        print("Esse número {} é nulo!".format(resultado))
    elif resultado % 2 == 0:
        print("O número {} é par!".format(resultado))
    else:
        print("O número {} é impar!".format(resultado))
    
    # POSITIVO OU NEGATIVO
    if resultado == 0:
        print("Esse número {} é nulo!".format(resultado))
    elif resultado > 0:
        print("O número {} é positivo!".format(resultado))
    else:
        print("O número {} é negativo!".format(resultado))

    # INTEIRO OU DECIMAL
    if resultado == 0:
        print("Esse número é nulo!")
    elif resultado // 1 == resultado:
        print("O número {} é inteiro!".format(resultado))
    else:
        print("O número {} é decimal!".format(resultado))

elif operacao == "-":
    resultado = num1 - num2
    # PAR OU ÍMPAR
    if resultado == 0:
        print("Esse número {} é nulo!".format(resultado))
    elif resultado % 2 == 0:
        print("O número {} é par!".format(resultado))
    else:
        print("O número {} é impar!".format(resultado))
    
    # POSITIVO OU NEGATIVO
    if resultado == 0:
        print("Esse número {} é nulo!".format(resultado))
    elif resultado > 0:
        print("O número {} é positivo!".format(resultado))
    else:
        print("O número {} é negativo!".format(resultado))

    # INTEIRO OU DECIMAL
    if resultado == 0:
        print("Esse número é nulo!")
    elif resultado // 1 == resultado:
        print("O número {} é inteiro!".format(resultado))
    else:
        print("O número {} é decimal!".format(resultado))

elif operacao == "/":
    resultado = num1 / num2
    # PAR OU ÍMPAR
    if resultado == 0:
        print("Esse número {} é nulo!".format(resultado))
    elif resultado % 2 == 0:
        print("O número {} é par!".format(resultado))
    else:
        print("O número {} é impar!".format(resultado))
    
    # POSITIVO OU NEGATIVO
    if resultado == 0:
        print("Esse número {} é nulo!".format(resultado))
    elif resultado > 0:
        print("O número {} é positivo!".format(resultado))
    else:
        print("O número {} é negativo!".format(resultado))

    # INTEIRO OU DECIMAL
    if resultado == 0:
        print("Esse número é nulo!")
    elif resultado // 1 == resultado:
        print("O número {} é inteiro!".format(resultado))
    else:
        print("O número {} é decimal!".format(resultado))

elif operacao == "*":
    resultado = num1 * num2
    # PAR OU ÍMPAR
    if resultado == 0:
        print("Esse número {} é nulo!".format(resultado))
    elif resultado % 2 == 0:
        print("O número {} é par!".format(resultado))
    else:
        print("O número {} é impar!".format(resultado))
    
    # POSITIVO OU NEGATIVO
    if resultado == 0:
        print("Esse número {} é nulo!".format(resultado))
    elif resultado > 0:
        print("O número {} é positivo!".format(resultado))
    else:
        print("O número {} é negativo!".format(resultado))

    # INTEIRO OU DECIMAL
    if resultado == 0:
        print("Esse número é nulo!")
    elif resultado // 1 == resultado:
        print("O número {} é inteiro!".format(resultado))
    else:
        print("O número {} é decimal!".format(resultado))

else:
    print("Operação inválida!")