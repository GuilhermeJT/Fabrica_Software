'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles'''

num = int(input('Digite um número:\n'))
num2 = int(input('Digite o segundo número:\n'))

for numero in range (num+1, num2):
    print(numero)