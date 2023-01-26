'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

cont = 1
resultado = 1

numero = int(input('Digite o número que você quer fatorar:\n'))
if numero > 1:
    while cont <= numero:
        resultado *= cont
        cont += 1
    print(resultado)

else:
    print('ERRO!')

