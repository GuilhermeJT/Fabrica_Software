'''Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0,
 que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 

Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos 
concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos        %
-------------------          -----         ---
Windows Server           1500        17%
Unix                              3500        40%
Linux                            3000         34%
Netware                       500           5%
Mac OS                        150           2%
Outro                           150           2%
-------------------         -----
Total                            8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.'''
votosWindows = []
votosUnix = []
votosLinux = []
votosNetware = []
votosMac = []
votosOutros = []
votosTotal = []

while True:
    print('''1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro''')
    voto = int(input('Qual o melhor Sistema Operacional para uso em servidores? '))
    print(50 * '=')
    print()
    if voto == 0:
        break

    else:
        if voto != 1 and voto != 2 and voto != 3 and voto != 4 and voto != 5 and voto != 6:
            print('Número inválido')
            print(50 * '=')
            print()

        else:
            votosTotal.append(voto)

            match voto:

                case 1:
                    votosWindows.append(voto)               
               
                case 2:
                    votosUnix.append(voto)

                case 3:
                    votosLinux.append(voto)

                case 4:
                    votosNetware.append(voto)

                case 5:
                    votosMac.append(voto)

                case 6:
                    votosOutros.append(voto)

porWindows = (len(votosWindows) * 100) / len(votosTotal)            
porUnix = (len(votosUnix) * 100) / len(votosTotal)
porLinux = (len(votosLinux) * 100) / len(votosTotal)
porNetware = (len(votosNetware) * 100)/ len(votosTotal)
porMac = (len(votosMac) * 100)/ len(votosTotal)
porOutros = (len(votosOutros) * 100)/ len(votosTotal)


print('Sistema Operacioal      Votos            %')
print(50 * '=')
print(f'Windows                   {len(votosWindows)}             {int(porWindows)}%')
print(f'Unix                      {len(votosUnix)}             {int(porUnix)}%')
print(f'Linux                     {len(votosLinux)}             {int(porLinux)}%')
print(f'Neware                    {len(votosNetware)}             {int(porNetware)}%')
print(f'Mac OS                    {len(votosMac)}             {int(porMac)}%')
print(f'Outros                    {len(votosOutros)}             {int(porOutros)}%')
print(50 * '=')
print(f'Total                           {len(votosTotal)}')
