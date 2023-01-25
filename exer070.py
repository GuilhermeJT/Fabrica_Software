'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos.
 Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m
Resultado final:
Rodrigo Curvêllo: 5.9 m'''

import math

saltos_nome = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
melhor = pior = media = 0

saltos = [ 0.0, 0.0, 0.0, 0.0 , 0.0]

while True:
    nome = str(input('Digite o nome do Atleta ou aperte ENTER para encerrar: '))
    if nome == '':
        break
    
    else:
        for c in range (0, 5):
            saltos[c] = float(input(f'{saltos_nome[c]} salto: '))

        melhorSalto = max(saltos)
        piorSalto = min(saltos)
        media = (saltos[0] + saltos[1] + saltos[2] + saltos[3] + saltos[4]) - (melhorSalto + piorSalto) / 3

                     
        print(30 * '=')
        print(f'Melhor salto {melhorSalto}\nPior salto {piorSalto}\nMedia dos saltos {media}')
        print(f'Resultado Final:\n{nome} : {media} m')
        print(30 * '=')
    
    
    
    
    