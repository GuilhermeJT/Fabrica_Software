'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

num = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))
real = float(input('Digite o numero real: '))

primeiro = num * 2 * (num2 / 2)
segundo = (num * 3) + real
terceiro = real * real * real

print(f'{primeiro:.2f}')
print(f'{segundo:.2f}')
print(f'{terceiro:.2f}')

