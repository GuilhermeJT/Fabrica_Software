'''A fábrica de refrigerantes Gui-Cola vende seu produto em três formatos: lata de 350 ml, garrafa de 600 ml e garrafa de 2 litros. 
Se um comerciante compra uma determinada quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.'''

lata = int(input('Quantas latas você quer: '))
garrafa = int(input( 'Quantas garrafas de 600ml: '))
garrafaL = int(input('Quantas garrafas de 2L: '))

litrosLata = lata * 350 / 1000
litrosGa = garrafa * 600 / 1000
garrafaL = garrafaL * 2

total = litrosLata + litrosGa + garrafaL

print(f'{total}L comprados')