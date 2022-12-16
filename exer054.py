contador = 0

while True:
    num = int(input('Número:\n'))
    if num == 0:
        break

    elif num == 50:
        contador = contador + 1

print(f'O número 50 apareceu {contador} vezes')
