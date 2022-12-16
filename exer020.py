'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

ano = int(input('Coloque o numero correspondente ao ano: '))

if (ano % 4) == 0 and (ano % 100) != 0:
    print('esse ano é bissexto')

else:
    print('Esse ano não é bissexto')
