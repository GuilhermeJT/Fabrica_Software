'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

vet1 = []
vet2 = []
vet3 = []

for i in range (5):
    vet1.append(int(input(f'Digite o número {i+1} da lista 1: ')))

for i in range(5):
    vet2.append(int(input(f'Digite o número {i+1} da lista 2: ')))

for i in range(5):
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print(vet3)