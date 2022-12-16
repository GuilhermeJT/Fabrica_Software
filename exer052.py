'''Ler diversos números e exibir quantos foram digitados. O valor -1 é código de  fim de entrada.'''

contador = 0
while True:
    num = float(input('Número:\n'))
    if num == -1:
        break
    contador = contador + 1

print(f'Foram digitados {contador} números')
