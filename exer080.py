'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''

idades = []
alturas = []

for c in range (5):
    idades.append(int(input('Digite sua idade: ')))    
    alturas.append(float(input('Digite sua altura: ')))
    print(50 * '=')

for c in range (-1, -6,-1):
    print(idades[c], end = ' ')
    print(alturas[c], end = ' ')



