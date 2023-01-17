'''O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros comprados a cada bimestre. Os pontos são atribuídos da seguinte forma:
•Se um cliente comprar 0 livros, ele ganhará 0 pontos.
•Se um cliente comprar um livro, ele ganhará 5 pontos.
•Se um cliente comprar dois livros, ele ganhará 15 pontos.
•Se um cliente comprar 3 livros, ele ganhará 30 pontos.
•Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
Lista de brindes:
De 20 à 30 pontos o cliente poderá escolher entre: Uma EcoBag OU Caneta personalizada
De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira.
Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00) OU Powerbank'''

primeiroMes = int(input('Quantos livros o cliente comprou no primeiro mês do bimestre:\n '))
segundoMes = int(input('Quantos livros o cliente comprou no segundo mês do bimestre:\n'))

if primeiroMes == 0:
    primeiroMes = 0

elif primeiroMes == 1:
    primeiroMes = 5

elif primeiroMes == 2:
    primeiroMes = 15

elif primeiroMes == 3:
    primeiroMes = 30

else:
    primeiroMes = 60

if segundoMes == 0:
    segundoMes = 0

elif segundoMes == 1:
    segundoMes = 5

elif segundoMes == 2:
    segundoMes = 15

elif segundoMes == 3:
    segundoMes = 30

else:
    segundoMes = 60
    

pontos = primeiroMes + segundoMes

if  20 <= pontos <= 30:
    print(f'Seus pontos sâo {pontos} pontos e você pode escolher entre uma EcoBag ou uma caneta personalizada!!')

elif    35 <= pontos <= 60:
     print(f'Seus pontos sâo {pontos} pontos e você pode escolher entre um livro de até R$30,00 ou uma Luminária de cabeceira')

else:
     print(f'Seus pontos sâo {pontos} pontos e você pode escolher entre  2 livros de até R$100,00 ou uma Powerbank')