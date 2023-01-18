'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. 
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67'''

valor = float(input('Qual o valor da compra:\n'))

print(f'{valor}  0      1 {valor }')
print(f'{valor}  {(valor * 10) / 100}  3 {valor + (valor * 10) / 100}')
print(f'{valor}  {(valor * 15) / 100}  6 {valor + (valor * 15) / 100}')
print(f'{valor}  {(valor * 20) / 100}  9 {valor + (valor * 20) / 100}')
print(f'{valor}  {(valor * 25) / 100} 12 {valor + (valor * 25) / 100}')