'''Faça um algoritmo que leia o nome de um aluno, o nome da disciplina, nota
de 3 provas e calcule a média desse aluno e verifique se o aluno foi aprovado. 
Sabendo que para ser aprovado a média deverá ser maior ou igual a 6,0.
Posteriormente imprima o resultado de cada variável linha abaixo de linha.'''

nome = input("Nome:")
disciplina = input("disciplina :")
nota = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota + nota2 + nota3)/3

if(media >= 6):
    print("sua media foi: ",media)
    print("Parabens, você foi aprovado!!")


else:
    print("reprovado")
