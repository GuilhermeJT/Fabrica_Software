'''Ler 20 números e exibir qual foi o menor e o maior informados.'''
contador = 0

while contador < 5:
    num = float(input('Digite um número: '))
    contador += 1

    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 

print(f'O maior número digitado é {maior} e o menor {menor}')

