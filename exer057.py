'''Um algoritmo em que usuário escolha uma opção de acordo com o último número da placa do carro e mostre uma mensagem dizendo em que dia da semana não poderá circular.'''

placa = int(input('Qual o último número da sua placa: \n'))

if placa == 0 or placa == 1 or placa == 2:
    print('Não circula Segunda-feira!!')

elif placa == 3 or placa == 4:
    print('Não circula na Terça-feira')

elif placa == 5 or placa == 6:
    print('Não cirucla na Quarta-feira')

elif placa == 6 or placa == 7:
    print('Não circula na Quinta-feira')

elif placa == 8 or placa == 9:
    print('Não circula na Sexta-feira')