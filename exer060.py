'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''

num = int(input('Digite um número para ver sua tabuada:'))

for i in range (1, 11):
    print(f'{num} x {i} ={num * i}')


