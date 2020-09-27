# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 
#   "Telefonou para a vítima?"
#   "Esteve no local do crime?"
#   "Mora perto da vítima?"
#   "Devia para a vítima?"
#   "Já trabalhou com a vítima?"
# 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

print("-"*30)
print(" INTERROGATÓRIO SOBRE O CRIME ")
print("-"*30)

count = 0
pergunta = input("Telefonou para a vítima? [SIM ou NÃO]: ")
pergunta.lower()
if pergunta == "sim":
    count += 1

pergunta = input("Esteve no local do crime? [SIM ou NÃO]: ")
pergunta.upper()
if pergunta == "sim":
    count += 1

pergunta = input("Mora perto da vítima? [SIM ou NÃO]: ")
pergunta.upper()
if pergunta == "sim":
    count += 1

pergunta = input("Devia para a vítima? [SIM ou NÃO]: ")
pergunta.upper()
if pergunta == "sim":
    count += 1

pergunta = input("Já trabalhou com a vítima? [SIM ou NÃO]: ")
pergunta.upper()
if pergunta == "sim":
    count += 1

if count == 2:
    print("Suspeito.")
elif count == 3 or count == 4:
    print("Cúmplice.")
elif count == 5:
    print("Assassino!")
else:
    print("Inocente.")


