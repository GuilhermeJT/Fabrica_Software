'''Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). O programa deve solicitar o valor da cotação do dólar.'''

cota = float(input('Qual a cotação atual do dólar:\nUS$'))
dolar = float(input('Quantos dolar você quer converter:\nUS$'))

final = dolar * cota
print(f'R${final:.2f} esse é o valor convertido em real')

