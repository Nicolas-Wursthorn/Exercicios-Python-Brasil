# Faça um programa que leia e valide as seguintes informações:
    # Nome: maior que 3 caracteres;
    # Idade: entre 0 e 150;
    # Salário: maior que zero;
    # Sexo: 'f' ou 'm';
    # Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite o seu nome: ")

while len(nome) <= 3:
    nome = input("Digite o seu nome (mínimo 4 letras): ")

idade = int(input("Digite sua idade: "))

while idade <= 0 or idade > 150:
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite o valor do seu salário: "))

while salario <= 0:
    salario = float(input("Digite o valor do seu salário: "))

sexo = input("Qual o seu gênero (F ou M): ").upper()

while sexo != 'F' and sexo != 'M':
    sexo = input("Qual o seu gênero (F ou M): ").upper()

estado_civil = input("Digite seu estado civil ('S', 'C', 'V', 'D'):").upper()

while (estado_civil != 'S') and (estado_civil != 'C') and (estado_civil != 'V') and (estado_civil != 'D'):
    estado_civil = input("Digite seu estado civil ('S', 'C', 'V', 'D'):").upper()


