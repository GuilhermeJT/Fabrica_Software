'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhes contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e reajuste-o seguindo o seguinte critério baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Qual seu salario atual: '))

if (salario > 0) and (salario <= 280):
    por = (20 * salario) / 100
    atual = salario + por

    print(f'{salario:.2f}')
    print(f'porcentual de aumento 20%')
    print(f'Valor do aumento R${por:.2f}')
    print(f'Salario atual {atual:.2f}')

elif (salario > 280) and (salario <= 270):
    por = (15 * salario) / 100
    atual = salario + por

    print(f'{salario:.2f}')
    print(f'porcentual de aumento 15%')
    print(f'Valor do aumento R${por:.2f}')
    print(f'Salario atual {atual:.2f}')

elif (salario > 700) and (salario <= 1500):
    por = (10 * salario) / 100
    atual = salario + por

    print(f'{salario:.2f}')
    print(f'porcentual de aumento 10%')
    print(f'Valor do aumento R${por:.2f}')
    print(f'Salario atual {atual:.2f}')

else:
    por = (5 * salario) / 100
    atual = salario + por

    print(f'{salario:.2f}')
    print(f'porcentual de aumento 5%')
    print(f'Valor do aumento R${por:.2f}')
    print(f'Salario atual {atual:.2f}')