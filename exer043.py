'''Dani tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. 
Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total 
economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda 
moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero.'''

moeda = [1, 5, 10, 25 , 50,]
um = int(input('Quantas moedas de 1 centavos: '))
cinco = int(input('Quantas modas de 5 centavos: '))
dez = int(input('Quantas moedas de 10 centavos: '))
vinte = int(input('Quantas moedas de 25 centavos: '))
cinquen = int(input('Quantas moedas de 50 centavos: '))
real = int(input('Quantas moedas de 1 real: '))

tum = um * moeda[0] / 100
tcinco = cinco * moeda[1] / 100
tdez = dez * moeda[2] / 100
tvinte = vinte * moeda[3] / 100
tcinquen = cinquen * moeda[4] / 100

total = tum + tcinco + tdez + tvinte + tcinquen + real

print(total)