'''Faça um algoritmo que o usuário possa digitar o seu nome e a sua idade. 
Utilizando a tabela a baixo, verifique em qual item se enquadra a idade da pessoa e escreva a mensagem:
(nome)  está com (idade) e pela tabela é considerado um (tipo)'''

nome = input("Nome: ")
idade = int(input("Idade: "))

if idade < 0:
    print(f'Está idade {idade} não existe')

elif 0 < idade <= 2:
    print("{} esta com {} ano e pela tabela é considerado um bebê".format(nome, idade))

elif 3 <= idade <= 11:
    print("{} esta com {} anos e pela tabela é considerado um criança".format(nome, idade))

elif 12 <= idade <= 21:
    print(f'{nome} esta com {idade} anos e pela tabela é considerado um jovem')

elif 22 <= idade <= 64:
    print(f'{nome} esta com {idade} anos e pela tabela é considerado um adulto')

elif (idade >= 65) and (idade <= 100):
    print(f'{nome} esta com {idade} anos e pela tabela é considerado um idoso')

else:
    print(f'{nome} esta com {idade} anos e ta com o pé na cova')



