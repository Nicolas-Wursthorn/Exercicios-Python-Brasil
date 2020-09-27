# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download

tamanhoMB = float(input("Qual o tamanho do arquivo para download (em MB)?: "))
velocidadeMbps = float(input("Qual a velocidade da internet (em MBps)?: "))

tempo = (tamanhoMB / velocidadeMbps) / 60

print("O tempo aproximado de download desse arquivo (em minutos) é: {}".format(tempo))