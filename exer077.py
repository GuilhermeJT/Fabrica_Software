'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''

contador = 0
caracteres = []
consoantes = []

for c in range (10):
    caracteres.append(str(input('Digite o caracter: ')))
    caracteres[c] = caracteres[c].upper()

for c in range(10):
    if caracteres[c] != 'A' and caracteres[c] != 'E' and caracteres[c] != 'I' and caracteres[c] != 'O' and caracteres[c] != 'U':
        contador += 1 
        consoantes.append(caracteres[c])

print(f'Foram digitadas {contador} consoantes')
        
for c in range (len(consoantes)):
        print(consoantes[c], end = ' ')

    
