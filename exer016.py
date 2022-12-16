num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
#maior
if (num1 > num2) and (num1 > num3):
    print(f'{num1} é o maior número')

elif (num2 > num1) and (num2 > num3):
    print(f'{num2} é o maior número')

else :
    print(f'{num3} é o maior número')

#menor

if(num1 < num2) and (num1 < num3):
    print(f'{num1} O número menor é ')

elif(num2 < num1) and (num2 < num3):
    print(f'{num2} O número menor é ')

else:
    print(f'{num3} O número menor é ')

