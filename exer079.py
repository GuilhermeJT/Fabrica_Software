'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

medias = []
mediasMaior = 0

for i in range (10):
    media = 0
    for c in range(4):
        media += float(input(f'Digite a nota {c+1} do aluno {i+1} :'))
    print(50 * '=')
    media /= 4

    medias.append(media)

    if media >= 7:
        mediasMaior += 1

print(f'O número de alunos com a média maior ou igual a 7.0 : {mediasMaior}')