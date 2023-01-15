'''Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante para uma pessoa (Coloque no mínimo 5 opções e máximo 10 opções de cardápio. 
Ex: Bife acebolado R$15,00; Lasanha R$25,00). A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao 
suário, “Aceita pagar a gorjeta do garçom 10% sobre o valor do prato”. Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), caso contrário, mostrar
 o valor final (somente o valor do prato)'''

print(28 * '-')
print('            MENU')
print(28 * '-')
print('''BIFE ACEBOLADO = R$15,00 [1]
LASANHA        = R$20,00 [2]
BOBÓ           = R$10,00 [3]
STROGONO       = R$12,00 [4]
CARRETEIRO     = R$20,00 [5]''')
print(28 * '-')

prato = int(input('Digite o código respectivo ao seu prato de escolha\n'))

match prato:
    case 1:
        prato = 15

    case 2:
        prato = 20

    case 3:
        prato = 10

    case 4:
        prato = 12

    case 5:
        prato = 20

gor = str(input('Aceita pagar a gorjeta de 10% sobre o valor do prato? \n'))
gor = gor.upper()
gor = gor.strip()[0]

if gor == 'S':
    por = 10 * prato / 100
    valorfinal = prato + por
    print(f'O valor ficou de {valorfinal}')

elif gor == 'N':
    print (f'O valor final é de {prato}')


