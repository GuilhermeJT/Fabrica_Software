'''Ler diversos números e exibir qual foi a soma. O valor -999 é o código de fim da  entrada. '''
soma = 0
while True:
    num = float(input('Número:\n'))
    if num == -999:
        break
    soma = soma + num

print(f'A soma dos números deu: {soma:.2f}')
        