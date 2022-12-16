'''O cardápio da lanchonete Burgão é o seguinte:
ESPECIFICAÇÃO CÓDIGO PREÇO
Cachorro Quente 100 R$ 11,20
Ovo Simples     101  R$   8,30
Bauru com Ovo   102 R$ 11,50
Hambúrguer      103 R$ 16,20
Refrigerante    201 R$ 6,00
Suco            202  R$ 7,50
Água Mineral    203 R$ 4,70

Escreva um algoritmo que leia o código de um sanduíche e de uma bebida, e mostre o valor a pagar pelo cliente. Assuma as entradas corretas:'''
cachorro = 11.20
ovo = 8.30
bauru = 11.50
hambur = 16.20
refri = 6.00
suco = 7.50
agua = 4.70

sandu = int(input('Código sanduba:\n'))
bebida = int(input('Código bebida:\n'))

match sandu:
    case 100:
        sandu = cachorro

    case 101:
        sandu = ovo

    case 102:
        sandu = bauru

    case 103:
        sandu = hambur

match bebida:
    case 201:
        bebida = refri

    case 202:
        bebida = suco

    case 203:
        bebida = agua

soma = bebida + sandu
print(soma)






