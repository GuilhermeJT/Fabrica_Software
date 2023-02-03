'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:

#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;'''
soma = acimaMedia = abaixoSete = 0
valores = []
cont = 0 
while True:
    nota = float(input('Digite nota: '))

    if nota == -1:
        break
    
    else:
        valores.append(nota)
        cont += 1
        soma += nota
        media = soma / cont
       
        if nota < 7:
            abaixoSete += 1

for c in range(len(valores)):
    if valores[c] > media:
        acimaMedia +=1

print(50 * '=')
print(f'A quantidades de notas digitadas foi: {cont}')

print(50 * '=')       
for c in range(len(valores)):
    print(valores[c],end = ' ')
print()
print(50 * '=')

valores.reverse()
for c in range(len(valores)):
    print(f'{valores[c]}')
print(50 * '=') 

print(f'A soma das notas da {soma}')
print(50 * '=')

print(f'A média das notas da {media}')
print(50 * '=')

print(f'Notas acima da media: {acimaMedia}')
print(50 * '=')

print(f'Notas abaixo de 7: {abaixoSete}')




