'''Crie um algoritmo para uma empresa de transportes que, a partir do peso de uma encomenda fornecida pelo usuário, calcule o preço da remessa conforme a seguinte tabela:
peso da encomenda                valor
-----------------------------------------------------
500g ou menos                       R$1,10
-----------------------------------------------------
Mais de 500g, Mais não mais         R$2,20
2Kg
-----------------------------------------------------
Mais de 2Kg, Mais não mais          R$3,70
10Kg
-----------------------------------------------------
Mais de 10Kg                           R$5,00 mais R$3,80/Kg pelo peso de ultrapassar 10Kg'''

valor = 0
peso = float(input('Digite o peso da encomenda em gramas: '))

if   peso <= 500:
    valor = 1.1

elif peso <= 2000:
    valor = 2.20

elif peso <= 10000:
    valor = 3.70

elif peso > 10000:
     valor = 5
     dif = (peso - 10000) / 1000
     valorDif = dif * 3.8
     valor += valorDif
     
print(f'O valor pelo transporte da encomenda é R${valor:.2f}')

