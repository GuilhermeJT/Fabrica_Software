'''Três amigos, Joceyr, Thiago e Alexandre. decidiram rachar igualmente a conta de um bar.
Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, 
mas faça com que Joceyr e Thiago não paguem centavos. Ex: uma conta de R$101,53 resulta 
em R$33,00 para Joceyr, R$33,00 para Thiago e R$35,53 para Alexandre.'''

total = float(input('Qual o valor total da conta:\nR$'))
num = total // 3
ale = total - num * 2

print(f'Joceyr vai pagar R${num}\nThiago vai pagar R${num}\nAlexandre vai pagar {ale}')


