'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

from re import match

num = float(input('Digite um número:'))
num2 = float(input('Digite o segundo número:'))
print(f'-' * 20)
print(f'soma = + ')
print(f'subtração = - ')
print(f'divisão = / ')
print(f'multiplicação = * ')
print(f'-' * 20)
operacao = input('Qual operação deseja realizar: ')


def teste():
    if res // 1 == res:
        print("Inteiro")
        if res % 2 == 0:
            print("Par")
            if res > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Impar")
    else:
        print("Decimal")
        if res % 2 == 0:
            print("Par")
            if res > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Impar")

match operacao:
    case '+':
        res = num + num2
        print(f'{num} + {num2} = {res}')
        teste()

    case '-':
        res = num - num2
        print(f'{num} - {num2} = {res}')
        teste()

    case '*':
        res = num * num2
        print(f'{num} * {num2} = {res}')
        teste()

    case '/':
        res = num / num2
        print(f'{num} / {num2} = {res}')
        teste()
