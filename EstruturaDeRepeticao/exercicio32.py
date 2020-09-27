# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperaturas = []

while True:
    graus = float(input("Digite a temperatura em graus (tecle 0 para parar): "))
    temperaturas.append(graus)
    media = sum(temperaturas) / len(temperaturas)

    if graus == 0:
        temperaturas.pop()
        print("A maior temperatura registrada: {}°C".format(max(temperaturas)))
        print("A menor temperatura registrada: {}°C".format(min(temperaturas)))
        print("A temperatura média registrada: {}°C".format(media))
        break