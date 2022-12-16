'''Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).'''

nome = str(input('Qual seu nome:\n'))
sexo = str(input('Sexo:[F/M]\n'))
print('Qual seu estado civil:\n')
print('1 - solteira \n2 - casada\n3 - divorciada')
estado = int(input(''))

sexo = sexo.upper()

if sexo == 'F' and estado == 2:
    tempo = int(input('Quantos anos você é casada:\n'))


