'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva: F - Feminino, M - Masculino ou Sexo Inválido.'''

sexo = input('Digite F para Feminino e M para masculino (em MAIUSCULO): ')
sexo = sexo.upper()

if sexo == 'F':
    print('Feminino')

elif sexo == 'M':
    print('Masculino')

else:
    print('Sexo invalido')
