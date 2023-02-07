'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas 
acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]
medias = [

]
for c in range(12):
    medias.append(float(input(f'\nDigite a temperatura média do més {meses[c]}: ')))

media = sum(medias) / 12

print(f'A média anual é {media}')

print('Os meses com a temperatura acima da média anual: ')
for c in range(12):
    if medias[c] > media:
        print(f'{c+1} - {meses[c]}')