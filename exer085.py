'''Escrever um algoritmo para ler a quantidade de horas/aula de duas professor e o valor por hora recebido por cada uma. Mostrar na tela qual dos professores tem salário total maior.'''

prof1 = {
    'Nome' : '',
    'salario' : ''
}

prof2 = {
    'Nome' : '',
    'salario' : ''
}

prof1['Nome'] = str(input('Digite o nome da primeira professora: '))
hora = float(input('Quantas horas você trabalha: '))
valor = float(input('Qual o valor da sua hora trabalhada: '))
prof1['salario'] = hora * valor

print(50 * '=')

prof2['Nome'] = str(input('Digite o nome da segunda professora: '))
hora = float(input('Quantas horas você trabalha: '))
valor = float(input('Qual o valor da sua hora trabalhada: '))
prof2['salario'] = hora * valor


if prof1['salario'] > prof2['salario']:
    print(f"A professora {prof1['Nome']} tem o salário maior")

else:
     print(f"A professora {prof2['Nome']} tem o salário maior")



