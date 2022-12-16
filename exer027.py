'''O departamento de Educação Física deseja informatizar este setor e colocou à disposição os seguintes dados de 50 alunos: 
#Matrícula, sexo (M, F), altura (cm) e status físico (1-bom, 2-regular, 3-ruim) 
#Estes dados deverão ser lidos através de uma unidade de entrada qualquer. 
#Calcular e imprimir: 
#a) A quantidade de alunos do sexo feminino com altura superior a 170 cm. 
#b) A % de alunos do sexo masculino (em relação ao total de alunos do sexo masculino) cujo status físico seja bom.'''

hb = 0
mh = 0
i = 0
h = 0
while i < 50:
    matri = int(input('\nDigite sua matricula:'))
    sexo = input('Sexo[M/F]:')
    sexo = sexo.upper()
    alt = int(input('Qual sua altura em cm:'))
    if sexo == 'F' and alt > 170:
        mh = mh + 1
    status = int(input('Status fisico:'))
    if sexo == 'M' and status == 1:
        hb = hb + 1

    elif sexo == 'M' and status != 1:
        h = h + 1

    else:
        h = h

    i = i + 1

soma = hb + h
por = (hb * 100)/soma
print(f'Existem {mh} mulheres acima de 170cm')
print(f'Porcentagem de homens com fisico bom {por}% em relação ao total de homens')











