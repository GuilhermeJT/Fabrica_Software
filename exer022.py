'''Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.'''

valor = float(input('Digite o preço atual do produto:'))

desconto = (10 * valor) / 100
valor_final = valor - desconto

print(f'O valor do produto com desconto de 10% ficou R${valor_final:.2f}')
