'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares'''

contador = 0
par = 0
impar = 0

while contador < 5:
    num = int(input('Número:\n'))
    contador += 1

    if num % 2 == 0:
        par += 1

    else:
        impar += 1

print(f'Tem {par} pares e {impar} ímpares')



