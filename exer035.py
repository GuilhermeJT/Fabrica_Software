"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                    Até 5 Kg              Acima de 5 Kg
File Duplo      R$ 34,90 por Kg          R$ 35,80 por Kg
Alcatra         R$ 44,90 por Kg          R$ 46,80 por Kg
Picanha         R$ 66,90 por Kg          R$ 67,80 por Kg


Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar."""

from re import match

print('-' * 35)
print('BEM VINDO AO HIPERMERCADO TABAJARA')
print('-' * 35)
print('Qual tipo de carne:')
print('1- File Duplo\n2- Alcatra\n3- Picanha')
tp = int(input())

quantidade = float(input('Digite a quantidade que deseja comprar: '))
cartao = str(input('Realizara o pagamento no cartão tabajara? [sim/não]'))
cartao = cartao.upper()

if tp == 1:
    nome = 'File Duplo'
    if quantidade <= 5:
        preco = quantidade * 34.90

    else:
        preco = quantidade * 35.80

elif tp == 2:
    nome = 'Alcatra'
    if quantidade <= 5:
        preco = quantidade * 44.90

    else:
        preco = quantidade * 46.80

elif tp == 3:
    nome = 'Picanha'
    if quantidade <= 5:
        preco = quantidade * 66.90

    else:
        preco = quantidade * 67.80

if cartao == 'SIM':
    des = (preco * 5) / 100
    final = preco - des

elif cartao == 'NÃO':
    des = 0
    final = preco


print('-' * 15)
print('CUMPOM FISCAL')
print(f'---{nome}')
print(f'---{quantidade:.2f}')
print(f'---{preco:.2f}')
print(f'---{final:.2f}')
print(f'---{des}')
print('-' * 15)