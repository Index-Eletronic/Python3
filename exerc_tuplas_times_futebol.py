'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

print('=-' * 50)
print('TABELA BRASILEIRÃO')
print('-=' * 50)

times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino', 'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá'
         , 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo', 'Sport')

print(f'O 5 primeiros classificados são: {times[0:5]}')
print('-=' * 50)
print(f'Os 4 ultimos colocados das Tabela são: {times[-4:]}')
print('-=' * 50)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 50)
print(f'O time da Chapecoense está na posição {times.index("Chapecoense")} da tabela.')