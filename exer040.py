'''João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas.
Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta.
Faça um algoritmo que calcule e mostre quanto restará do salário do João '''

salario = 1200
c1 = 200
c2 = 120

por1 = c1 * 2 / 100
por2 = c2 * 2 / 100

c1 = c1 + por1
c2 = c2 + por2

total = c1 + c2
final = salario - total
print(final)