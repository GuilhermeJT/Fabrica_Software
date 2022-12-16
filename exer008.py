'''Faça um algoritmo que calcule o custo estimado de uma viagem de carro.
Posteriormente imprima o resultado.'''

distancia = int(input("Informe a distancia que você vai percorrer em km: "))
media = int(input("Quanto seu carro usa de gasolina por quilometro rodado:"))
gasolina = float(input("Qual a valor do litro de gasolina: "))

disMed = distancia / media
custo = disMed * gasolina

print("O custo vai ser de : {:.2f} reais".format(custo))