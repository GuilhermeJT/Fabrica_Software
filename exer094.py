'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''

idades = []
alturas = []
contador = 0 

for c in range (30):
    idades.append(int(input('Digite a idade do aluno: ')))
    alturas.append(float(input('Digite a altura em cm: ')))
    print()

mediaTotal = sum(alturas) / 30

for i in range(30):
    if idades[i] > 13:
        if alturas[i] < mediaTotal:
            contador +=1


print(f'{contador} numero de alunos com mais de 13 anos e com a altura inferior a média total dos alunos da sala')