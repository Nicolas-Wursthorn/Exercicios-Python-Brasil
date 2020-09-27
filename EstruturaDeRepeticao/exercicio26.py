# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input("Digite a quantidade de turmas: "))
alunos = []
c = 1

while c < turmas:
    turma = int(input("Quantos alunos há na turma {}?: ".format(c)))
    if turma > 40:
        print("A turma não pode conter mais de 40 alunos.")
    else:
        alunos.append(turma)
        c += 1

media = sum(alunos) / len(alunos)

print("O número médio de alunos por turma é de {}".format(media))