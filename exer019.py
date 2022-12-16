''''Faça um Programa que peça os 3 lados de um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.'''

a = int(input('Digite um dos lados:'))
b = int(input('Digite outro lado:'))
c = int(input('Digite o ultimo lado:'))

if (a == 0) or (b == 0) or (c == 0) or (a + b < c) or (a + c < b) or (b + c < a):
    print('Esses valores não formam um triângulo')

elif (a > b == c) or (b > a == c) or (c > a == b):
    print('Esse é um triângulo isósceles')

elif a == b and b == c:
    print('Esse é um triângulo equilátero')

else:
    print('Esse é um triângulo escaleno')
