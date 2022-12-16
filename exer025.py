'''Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, 
cada uma sendo vendida respectivamente por R$10,00, R$12,00 e R$15,00. 
Faça um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, 
médias e grandes referentes a uma venda, o algoritmo informe qual o valor total da compra.'''

pequena = int(input('Quantas camisetas pequenas você quer: '))
media = int(input('Quantas camisetas medias você quer: '))
grande = int(input('Quantas camisetas grandes você quer: '))

pequena = pequena * 10
media = media * 12
grande = grande * 15

soma = pequena + media + grande

print(f'Valor total da compra vai ser de {soma}')
