# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou v-Vespertino ou n-Noturno. Imprima a mensagem "Bom dia", "Boa Tarde" ou "Boa Noite" ou "Valor Inválido!" conforme o caso.

turno = input("Em qual turno você estuda?\n M - Matutino, V - Vespertino ou N - Noturno: ")

if turno == "M":
	print("Bom Dia!")
elif turno == "V":
	print("Boa Tarde!")
elif turno == "N":
	print("Boa Noite!")
else:
	print("Valor Inválido!")