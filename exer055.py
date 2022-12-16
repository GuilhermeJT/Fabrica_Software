'''Ler 20 números e exibir qual foi o menor e o maior informados.'''

contador = 0


num = float(input('Número:\n'))
maior = num
menor = num

while contador < 2:
    num = float(input('Número:\n'))

    contador = contador + 1
    if num > maior:
        maior = num

    elif num < maior:
        menor = num

    

print(maior, menor)