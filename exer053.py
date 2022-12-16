'''Ler diversos números e exibir quantos números ímpares foram digitados.  Considere o valor - 999 como código fim de entrada.'''
contador = 0
while True:
    num = float(input('Número:\n'))
    if num == -999:
        break
    elif num % 2 != 0:
        contador = contador + 1

print(f'Foram digitados {contador} números ímpares')
