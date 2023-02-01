'''Quando um bebê nasce, algumas informações são armazenadas sobre ele, tais como: nome, data do nascimento, peso do nascimento, altura, a mãe deste bebê e o médico que fez seu parto. 
Para as mães, o berçário também deseja manter um controle, guardando informações como: nome, endereço, telefone e data de nascimento. Para os médicos, é importante saber: CRM, nome, telefone celular e especialidade.'''

recem_nascido = {
    'nome' : '',
    'data_nascimento' : '',
    'peso_nascimento' : 0,
    'altura' : 0,
    'mae_bebe' : '',
    'medico_parto' : '',
    }

mae_recem_nascido  = {
    'nome' : '',
    'endereco' : '',
    'telefone' : 0,
    'data_nascimento' : ''   
}

medico_parto = { 
    'nome' : '',
    'crm' : 0,
    'telefone' : 0,
    'especialidade' : ''
}

print('ADICIONE DADOS DO RECÉM NASCIDO')
print(50 * '=')
recem_nascido['nome'] = str(input('Digite o nome do recém nascido: '))
recem_nascido['data_nascimento'] = str(input('Digite a data de nascimento: '))
recem_nascido['peso_nascimento'] = int(input('Digite o peso do nascimento em kg: '))
recem_nascido['altura'] = float(input('Digite a altura do recém nascido em cm: '))
recem_nascido['mae_bebe'] = str(input('Digite o nome da mãe do recém nascido: '))
recem_nascido['medico_parto'] = str(input('Digite o médico que fez o parto: '))
print(50 * '=')
print('ADICIONE DADOS DA MÃE')
mae_recem_nascido['nome'] = str(input('Digite o nome da mãe: '))
mae_recem_nascido['endereco'] = str(input('Digite o endereço (RUA): '))
mae_recem_nascido['telefone'] = int(input('Digite o número de telefone: '))
mae_recem_nascido['data_nascimento'] = str(input('Digite a data de nascimento da mãe: '))
print(50 * '=')
print('ADICIONE DADOS DO MÉDICO')
medico_parto['nome'] = str(input('Digite o nome do médico: '))
medico_parto['crm'] = int(input('Digite o CRM do médico: '))
medico_parto['telefone'] = int(input('Digite o número de telefone do médico: '))
medico_parto['especialidade'] = str(input('Digite a especialidade do médico: '))

print(recem_nascido)
print(mae_recem_nascido)
print(medico_parto)
