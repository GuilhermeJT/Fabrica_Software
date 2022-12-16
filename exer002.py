'''Faça um algoritmo que leia o nome e as notas dos 4 bimestres de um aluno.
Posteriormente imprima o resultado de cada variável linha abaixo de linha.'''

nome = input("Digite seu nome: ")
pri = int(input("Digite a nota do seu primeiro bimestre: "))
seg = int(input("Digite a nota do seu segundo bimestre: "))
ter = int(input("Digite a nota do seu terceiro bimestre: "))
quar = int(input("Digite a nota do seu quarto bimestre: "))

media = (pri + seg + ter + quar)/4

print(nome)
print(pri)
print(seg)
print(ter)
print(quar)
print(media)