'''Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 
a) a idade dessa pessoa em anos; 
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias; 
d) a idade dessa pessoa em semanas.'''

nascimento = int(input('Em que ano você nasceu?\n'))
atual = int(input('Qual o ano atual?\n'))

idade = atual - nascimento
dias = idade * 365
semanas = dias // 7

print(f'Sua idade é de {idade}')
print(f'Sua idade em dias é {dias}')
print(f'Sua idade em semanas é {semanas}')

