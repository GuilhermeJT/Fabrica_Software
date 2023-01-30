'''Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida receba um novo valor do usuário e verifique se este valor se encontra no vetor.'''

numeros = []
encontrou = False 

for c in range (3):
    numeros.append(int(input(f'Digite o número {c+1}: ')))

num = int(input('Número para verificar: '))

for c in range (len(numeros)):
    if num == numeros[c]:
        encontrou = True 
        break

if encontrou == True:
    print( f'O número {num} tem no Vetor')

else:
    print(f'O número {num} não tem no Vetor')


    