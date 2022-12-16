'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

gaso = 2.5
alcool = 1.9

combustivel = str(input('Gasolina[G] ou Álcool[A]: '))
combustivel = combustivel.upper()
litros = float(input('Quantos Litros: '))

if combustivel == 'G':
    if litros <= 20:
        preco = gaso - (gaso * 4) / 100 #gaso * 0,96
        total = litros * preco
        print(total)
    else:
        preco = gaso - (gaso * 6) / 100 #gaso * 0,94
        total = litros * preco
        print(total)

elif combustivel == 'A':
    if litros <= 20:
        preco = alcool - (alcool * 3) / 100
        total = litros * preco
        print(total)
    else:
        preco = alcool - (alcool * 5) / 100
        total = litros * preco
        print(total)
