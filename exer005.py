'''Faça um algoritmo que leia o nome do aluno, o nome da disciplina, notas de 3 provas e calcule a média desse aluno.
Posteriormente imprima o resultado de cada variável linha abaixo de linha.'''

nome = input("informe seu nome: ")
materia = input("informe o nome da materia: ")
nota = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))
nota3 = float(input("informe a terceira nota: "))

media = (nota + nota2 + nota3)/3

print("Media: {:.2f}".format( media))