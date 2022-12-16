'''Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. 
Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, 
calcule e mostre o valor da comissão e o salário final do funcionário.'''

salario = float(input('Digite seu salario fixo: '))
vendas = float(input('Digite o valor da suas vendas: '))

comi = (4 * vendas)/100
final = salario + comi

print(f'Sua comissão é de R${comi:.2f} e seu salario final é de R${final:.2f}')
