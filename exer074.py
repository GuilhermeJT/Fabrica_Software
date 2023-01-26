'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''

numeros = []

for c in range (5):
    numeros.append(int(input('Digite o número: ')))


for c in range (5):
    print(numeros[c], end = ' ')

    