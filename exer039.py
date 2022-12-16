'''Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano. Esqueça a questão
dos anos bissextos e considere sempre que um mês possui 30 dias.'''


dia = int(input('Dia:\n'))
mes = int(input('Mês:\n'))

if dia < 12 or mes < 30:
    passados = (mes * 30 -30) + dia
    print(passados)

elif dia > 30 or mes > 12:
    print('ERRO')

