# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input('Digite um número inteiro: '))
primos = []
divisoes = 2

for i in range(2, num+1):
    if i % 2 == 1 and i != 2:           # NÃO TERMINADO
        primos.append(i)
        divisoes += 1
    else:
        divisoes += 1
        

primos = str(primos).strip('[]')
print('Numéros primos entre 1 e {}: {}'.format(num, primos))
print('Número de divisões: {}'.format(divisoes))


    




        

