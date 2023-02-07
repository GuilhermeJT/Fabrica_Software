'''Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 
200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de
 defeito:

#necessita da esfera;
#necessita de limpeza;
#necessita troca do cabo ou conector;
#quebrado ou inutilizado 
Uma identificação igual a zero encerra o programa.'''

mouses = []
problemasTotal = []
problemaEsfera = []
problemaLimpeza = []
problemaTroca = []
quebrado = []

while True:
    num = int(input('Número de identificação do mouse: \n'))

    if num == 0:
        break

    else:
        mouses.append(num)

        print('1- necessita da esfera')
        print('2- necessita de limpeza')
        print('3- necessita troca do cabo ou conector')
        print('4- quebrado ou inutilizado')
        problema = int(input('Qual o problema do mouse: '))

        problemasTotal.append(problema)

        if problema == 1:
            problemaEsfera.append(problema)

        elif problema == 2:
            problemaLimpeza.append(problema)

        elif problema == 3:
            problemaTroca.append(problema)

        elif problema == 4:
            quebrado.append(problema)

porEsfera = ((len(problemaEsfera)) * 100) / len(problemasTotal)
porLimpeza  = ((len(problemaLimpeza)) * 100) / len(problemasTotal)
porTroca  = ((len(problemaTroca)) * 100) / len(problemasTotal)
porQuebrado  = ((len(quebrado)) * 100) / len(problemasTotal)


print(f'Quantidade de mouses: {len(problemasTotal)}')
print()

print('Situação:                                            Quantidade:                 Percentual:')
print(f'1- necessita da esfera                                   {len(problemaEsfera)}                          {porEsfera:.2f}%')
print(f'2- necessita de limpeza                                  {len(problemaLimpeza)}                          {porLimpeza:.2f}%')
print(f'3- necessita troca do cabo ou conector                   {len(problemaTroca)}                          {porTroca:.2f}%')
print(f'4- quebrado ou inutilizado                               {len(quebrado)}                          {porQuebrado:.2f}%')
 


