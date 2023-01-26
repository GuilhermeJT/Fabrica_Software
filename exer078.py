'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''

num = []
par = []
impar = []

for c in range(20):
    num.append(int(input('Digite o número: ')))
    if num[c] % 2 == 0:
        par.append(num[c])

    else:
        impar.append(num[c])

print(f'Vetor com todos os números : {num}')
print(f'Vetor par : {par}')
print(f'Vetor ímpar : {impar}')

