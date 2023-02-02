'''Uma máquina de vender café funciona da seguinte forma: o usuário seleciona um tipo de café, insere algumas notas ou moedas na máquina e, 
se a quantia paga for suficiente para pagar o face desejado, a máquina enche um copo descartável com o tipo de café selecionado e dá o num em moedas. 
Faça um programa para imitar esse comportamento: o usuário informa qual é o tipo de café desejado e o valor pago, e o seu programa deve dizer qual deve ser o valor do num 
e quantas moedas são necessárias para pagar esse num. Considere a existência de moedas com os seguintes valores: R$ 1.00, R$ 0.50, R$ 0.25, R$ 0.10, R$ 0.05 e R$ 0.01.A tabela de preços é dada abaixo:

tipo café             preço
---------------------------
normal                R$1,05
---------------------------
expresso             R$1,52
---------------------------
capuccino           R$2,17
---------------------------
mocaccino          R$2,36'''

print(30 * '=')
print('''normal    - R$1,05 - 1
expresso  - R$1,52 - 2
capuccino - R$2,17 - 3
mocaccino - R$2,36 - 4''')
print(30 * '=')
cafe = int(input('Qual café você quer: '))
valor = float(input('Com qual valor você ira pagar: R$'))

match cafe:
    case 1:
        valor_cafe = 1.05

    case 2:
        valor_cafe = 1.52

    case 3:
        valor_cafe = 2.17

    case 4:
        valor_cafe = 2.36

troco = valor - valor_cafe

if valor >= valor_cafe:
    num = valor - valor_cafe

    real = num // 1.0
    num = num - (real * 1.0)

    cinquenta = num // 0.5
    num = num - (cinquenta * 0.5)

    vinteCinco = num // 0.25
    num = num - (vinteCinco * 0.25)

    dez = num // 0.10
    num = num - (dez * 0.10)

    cinco = num // 0.05
    num = num - (cinco * 0.25)

    um = num // 0.01
else:
    print('ERRO!')

print(f'O valor do troco é de R${troco}')
print(f'Moedas de R$1 real = {real} ')
print(f'Moedas de R$0,50 centavos = {cinquenta}')
print(f'Moedas de R$0,25 centavos = {vinteCinco}')
print(f'Moedas de R$0,10 centavos = {dez}')
print(f'Moedas de R$0,05 centavos = {cinco}')
print(f'Moedas de R$0,01 centavos = {um}')
    