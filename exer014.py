'''Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
Após, calcule e escreva o saldo atual (saldo atual = saldo - débito + crédito). 
Também teste se saldo atual for maior ou igual a zero.
Em seguida escreva a mensagem 'Saldo Positivo', senão, escrever a mensagem 'Saldo Negativo'.'''

conta = int(input('Qual o número da sua conta:'))
saldo = float(input('Qual seu saldo:'))
debito = float(input('Débito:'))
credito = float(input('Crédito:'))

saldo_atual = (saldo - debito) + credito

if saldo_atual <= 0:
    print(f'Saldo atual da conta {conta} é de R${saldo_atual:.2f}, Saldo negativo')

else:
    print(f'Saldo atual da conta {conta} é de R${saldo_atual:.2f}, Saldo positivo')
