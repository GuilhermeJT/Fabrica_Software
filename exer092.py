'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

positivo = negativo = 0

print(30 * '=')
print('RESPONDA 1 - SIM, 2 - NÃO')

tele = int(input('Telefonou para a vítima? '))
if tele == 1:
    positivo += 1

esteve = int(input("Esteve no local do crime? "))

if esteve == 1:
    positivo += 1

moradia = int(input('Mora perto da vítima? '))

if moradia == 1:
    positivo += 1

dividia = int(input('Devia para a vítima? '))

if dividia== 1:
    positivo += 1


trabalho = int(input('Já trabalhou com a vítima? '))
if trabalho == 1:
    positivo += 1


if  1<= positivo <= 2:
    print('\nSuspeito')

elif 2 < positivo <= 4:
    print('\nCúmplice')

elif positivo == 5:
    print('\nAssasino')

else:
    print('\nInocente')