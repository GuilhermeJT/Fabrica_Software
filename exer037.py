pao = int(input('Quantos pães foi vendido hoje?\n'))
broa = int(input('Quantas broas foi vendido hoje?\n'))

finalBroa = broa * 3.50
finalTudo = finalBroa + pao
poupa = (finalTudo * 10) / 100

print(f'O valor total das vendas foi de R${finalTudo}\ne o valor para ser guardado na poupança é de R${poupa}')
