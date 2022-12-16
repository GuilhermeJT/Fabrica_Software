'''A lanchonete GostoSoft vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, 
uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 
50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a 
quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.'''

sanduba = int(input('Quantos sanduba ira fazer: '))

queijo = (sanduba * 100) / 1000
presunto = (sanduba * 50) / 1000
hamburguer = (sanduba * 100) / 1000

print(f'Precisa de {queijo}kg de queijo, {presunto}kg de presunto e {hamburguer} kg de Hambúrguer')
