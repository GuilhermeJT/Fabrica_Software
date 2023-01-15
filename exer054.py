'''Ler diversos números inteiros e exibir quantas vezes o número 50 foi  informado. O valor 0 é o código de fim de entrada. '''
contador = 0

while True:
    num = int(input('Número:\n'))
    if num == 0:
        break

    elif num == 50:
        contador = contador + 1

print(f'O número 50 apareceu {contador} vezes')
