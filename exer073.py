'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''

voto1 = voto2 = voto3 = voto4 = votoNulo = votoBranco = total = 0
nome1 = nome2 = nome3= nome4 = ''
while True:
    print(30 * '=')
    print('''
    1 - Jose
    2 - João
    3 - Eva
    4 - Rodrigo
    5 - Voto Nulo
    6 - Voto em Branco''')
    print(30 * '=')
    voto = int(input('Qual seu voto: '))
    
    if voto == 0:
        break

    else:
        
        total += 1
        nome1 = 'Jose'
        nome2 = 'João'
        nome3 = 'Eva'
        nome4 = 'Rodrigo'
        match voto:
            case 1:
                voto1 += 1
                
            case 2:
                voto2 += 1
                
            case 3:
                voto3 += 1
                
            case 4:
                voto4 += 1

            case 5:
                votoNulo += 1
                
            case 6:
                votoBranco += 1
            

print('\n')
print(30 * '=')          
print(f'''  
O candidato {nome1} teve {voto1} votos!
O candidato {nome2} teve {voto2} votos!
O candidato {nome3} teve {voto3} votos!
O candidato {nome4} teve {voto4} votos!
''')
print(f'Total de votos brancos : {votoBranco}')
print(f'Total de votos nulos : {votoNulo}\n')

porcentagemNulos = (votoNulo * 100)  / total
porcentagemBranco = (votoBranco * 100) / total


print(f'A porcentagem de votos nulos sobre o total de votos é {porcentagemNulos}%')
print(f'A porcentagem de votos brancos sobre o total de votos é {porcentagemBranco}%')
print(30 * '=')      
