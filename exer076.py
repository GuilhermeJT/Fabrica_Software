'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

soma = 0
notas = []

for c in range(1, 5):
    notas.append(float(input(f'Digite a nota {c}: ')))

    
for c in range (4):
    soma += notas[c]
    
media = soma / 4

print(f'Sua média é = {media}')