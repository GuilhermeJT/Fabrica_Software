'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). 
Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''


NumCarros = []
cidades = []
NumAcidentes = []
maior = menor = soma = media = soma2 = media2 = cont = 0

for c in range(3):
    cidades.append(int(input(f'Digite o nome da cidade {c+1}: ')))
    NumCarros.append(int(input(f'Digite o número de carros: ')))
    NumAcidentes.append(int(input(f'Digite o número de acidentes: ')))
    print(50 * '=')
    if c == 0:
        maior = menor = NumAcidentes[0]

    if NumAcidentes[c] > maior:
        maior = NumAcidentes[c]
        cidadeMaior = cidades[c]

    if NumAcidentes[c] < menor:
        menor = NumAcidentes[c]
        cidadeMenor = cidades[c]

    soma += NumCarros[c]

    if NumCarros[c] < 2000:
        soma2 += NumAcidentes[c]
        cont += 1


media = soma / 3
media2 = soma2 / cont

print(f'A cidade {cidadeMaior} tem o maior indice de acidentes: {maior}')
print(f'A cidade {cidadeMenor} tem o menor indice de acidentes: {menor}')
print(f'A media de veiculos das 5 cidades juntas é: {media:.2f}')
print(f'A media de acidentes das cidades com menos de 2000 veiculos é: {media2:.2f}')