# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

idades = []

while True:
    idade = int(input('Digite sua idade (caso queira parar tecle 0): '))
    idades.append(idade)

    if idade == 0:
        idades.pop()

        if len(idades) == 0:
            print("Infelizmente não conseguimos informações suficiente para concluir a pesquisa.")
            break

        media = sum(idades) / len(idades)
        if media > 0 and media <= 25:
            print("A sua turma é jovem!")
            break
        elif media > 26 and media <= 60:
            print("A sua turma é adulta!")
            break
        else:
            print("A sua turma é idosa!")
            break