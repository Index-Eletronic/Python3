'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
print('VALORES SORTEADOS: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no jogo')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #itemgetter ordena 0 ordem de chave 1 ordem de valor
print('-=' * 30)
print('-= RANKING DOS JOGADORES =-')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)