'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores'''
cont = maior = menor = soma = 0

while True:
    num = float(input('Número:\n'))
    cont += 1

    if cont == 1:
        maior = menor = num
    
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 

    soma += num

    pausa = str(input('Quer continuar, se sim digite S\nSe quer parar, digite P\n'))
    pausa = pausa.upper()
    pausa = pausa.strip()[0]
    
    if pausa == 'P':
        break;

    

print(f'O menor valor foi {menor}\nO maior valor foi {maior}\nA soma desses números da {soma}')