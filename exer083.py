'''Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela. Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.'''

numeros = []
soma = 0

for c in range(5):
    numeros.append(int(input(f'Digite o número {c + 1}: ')))
    soma += numeros[c]


print(f'Resultado da soma desses números: {soma}')

for i in range(len(numeros)):
    print(numeros[i])

