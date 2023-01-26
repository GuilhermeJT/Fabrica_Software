'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''

numeros = []

for c in range (10):
    numeros.append(float(input('Digite o número: ')))

for c in range(-1, -11, -1):
    print(numeros[c])

