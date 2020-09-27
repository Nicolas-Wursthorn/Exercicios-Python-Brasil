# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
	# 1. A mensagem "Aprovado", se a média for maior ou igual a sete;
	# 2. A mensagem "Reprovado", se a média for menor do que sete;
	# 3. A mensagem "Aprovado com Distinção ", se a média for igual a dez.

m1 = float(input("Digite a primeira nota: "))
m2 = float(input("Digite a segunda nota: "))

media = (m1 + m2) / 2

if media == 10:
	print("Aprovado com Distinção.")
elif media >= 7:
	print("Aprovado.")
else:
	print("Reprovado.")