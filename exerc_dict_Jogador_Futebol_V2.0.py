'''
Aprimore o desafio Jogador de Futebol para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''


jogador = dict()
partidas = list()
time = list()
#============================= LER OS DADOS DE VÁRIOS JOGADORES ======================================
while True:
    jogador.clear() # Vai limpar o cadastro para receber um novo jogador
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear() # Vai limpar a partida para receber novos numeros.
    for c in range(0, tot): # Cria um contador para inserir o numero de gols
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas [:] # Lista Partidas recebe uma cópia de Dicionario jogador
    jogador['total'] = sum(partidas) # O total recebe a soma das lista partidas [sum =  soma]
    time.append(jogador.copy()) # O time recebe uma copia de jogador.
    while True:
        resp = str(input(' Quer Continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S OU N')
    if resp == 'N':
        break
#============================= ANALISAR OS DADOS E MOSTRAR ===========================================
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)

print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
#============================= FAZER UMA BUSCA E MOSTRAR OS DADOS ===========================================
while True:
    busca = int(input('Mostrar os dados de qual Jogador? [ 999 para parar ]'))
    if busca == 999:
        break
    if busca >= (len(time)):
        print(f'Não existe jogador com o código: {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f' NO JOGO {i+1} fez {g} Gols.   ')
    print('-=' * 40)
print('<< VOLTE SEMPRE>>')