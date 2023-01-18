'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

login = str(input('Digite seu nome de usúario:\n'))
senha = str(input('Digite sua senha:\n'))

while login == senha:
        print('ERRO!')
        login = str(input('Digite seu nome de usúario:\n'))
        senha = str(input('Digite sua senha:\n'))

