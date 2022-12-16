'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220)  : R$ 1100,0

(-) IR (5%)               : R$   55,00  
(-) INSS ( 10%)           : R$  110,00
FGTS (11%)                : R$  121,00
Total de descontos        : R$  165,00
Salário Liquido           : R$  935,00'''

hora = float(input('Quantas horas você trabalha no mês: '))
valor = float(input('Qual o valor da sua hora: '))

salario = hora * valor

if (salario > 0) and (salario <= 900):
    inss = (10 * salario) / 100
    fgts = salario * 0.10

    liquido = salario - inss

    print(f'Salário liquido é de {liquido:.2f} e teve descondo de {inss:.2f}')

elif (salario > 900) and (salario <= 1500):
    ir = (5 * salario) / 100
    inss = (10 * salario) / 100
    fgts = (11 * salario) / 100

    desconto = ir + inss
    liquido = salario - desconto

    print(f'Salário liquido é de {liquido:.2f} e teve desconto de {desconto}')

elif (salario > 1500) and (salario <= 2500):
    ir = (10 * salario) / 100
    inss = (10 * salario) / 100
    fgts = (11 * salario) / 100

    desconto = ir + inss
    liquido = salario - desconto

    print(f'Salário liquido é de {liquido:.2f} e teve desconto de {desconto}')

else:
    ir = (20 * salario) / 100
    inss = (10 * salario) / 100
    fgts = (11 * salario) / 100

    desconto = ir + inss
    liquido = salario - desconto

    print(f'Salário liquido é de {liquido:.2f} e teve desconto de {desconto}')
