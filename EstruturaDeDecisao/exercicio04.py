# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ".lower())

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'u':
	print("Essa letra é uma vogal!")
else:
	print("Essa letra é uma consoante!")
