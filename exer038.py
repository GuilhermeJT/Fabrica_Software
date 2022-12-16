'''O restaurante a quilo Sabor em Quilo cobra R$59,00 por cada quilo de refeição.
Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.'''

peso = float(input('Qual o peso do prato:\n'))

valor = peso * 59
print(f'O valor a pagar é de R${valor}')