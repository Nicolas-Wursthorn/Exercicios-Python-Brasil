# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

#BOLSONABO 18
#LULAMOTOSCO 14
#FAUSTINHO 10

num_eleitores = int(input("Digite o número total de eleitores: "))

bolsonabo = 0
lulamotosco = 0
faustinho = 0
votos = {}

for i in range(num_eleitores):
    voto = int(input("Digite o seu voto: "))
    if voto == 18:
        bolsonabo += 1
    elif voto == 14:
        lulamotosco += 1
    elif voto == 10:
        faustinho += 1
    else:
        print("Número de candidato inválido, por favor, vote novamente.")


print("=== VOTAÇÃO ENCERRADA === ")
print("VOTOS BOLSONABO: {}".format(bolsonabo))
print("VOTOS LULAMOTOSCO: {}".format(lulamotosco))
print("VOTOS FAUSTINHO: {}".format(faustinho))