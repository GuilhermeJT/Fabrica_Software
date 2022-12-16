'''Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição: 
Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser vendido por um preço 45% maior, caso 
contrário o lucro será de 30%. Sabendo disso, faça um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.'''

compra = float(input('Qual foi o valor de aquisição: '))

if 0 < compra < 50:

    por = (compra * 45) / 100
    final = compra + por
    print(f'O valor de venda vai ser de R${final:.2f}')

elif compra >= 50:

    por = (compra * 30) / 100
    final = compra + por
    print(f'O valor de venda vai ser de R${final:.2f}')

else:

    print('Esse número não existe')
