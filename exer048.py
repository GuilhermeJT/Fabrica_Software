'''Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento.
Utilize os códigos da tabela a seguir para ler qual condição de pagamento escolhida e efetuar o cálculo adequado.Código Condição de pagamento:
1 - À vista em dinheiro ou pix, recebe 10% de desconto;
2 - À vista no cartão de crédito, recebe 5% de desconto
3 - Em duas vezes, preço normal de etiqueta sem juros
4 - Em três vezes, preço normal de etiqueta mais juros de 10%'''

preco = float(input('Qual preço:\n'))
print('-'*60)
print('FORMAS DE PAGAMENTO')
print('1 - À vista em dinheiro ou pix\n2 - À vista no cartão de crédito\n3 - cartão de crédito em duas vezes\n4 - cartão de crédito em três vezes')
num = int(input())

match num:
    case 1:
        des = preco * 10 / 100
        preco = preco - des
        print(f'Valor a ser pago é de {preco:.2f}')

    case 2:
        des = preco * 5 / 100
        preco = preco - des
        print(f'Valor a ser pago é de {preco:.2f}')

    case 3:
        print(f'Valor a ser pago é de {preco:.2f}')

    case 4:
        juros = preco * 10 / 100
        preco = preco + juros
        print(f'Valor a ser pago é de {preco:.2f}')
