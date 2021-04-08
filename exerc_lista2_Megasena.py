'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint

lista = list()
jogos = list()
print('-=' * 30)
print(f' {"PALPITES PARA MEGASENA":^30} ')
print('-=' * 30)
quant = int(input('QUANTOS JOGOS VOCÊ QUER FAZER? '))
tot = 1
while tot <= 0:
    cont = 0
    with True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS','-=' * 3)
print(jogos)
#for i, l in enumerate(jogos):
     #print(f'JOGO: {i+1}: {l:^3}')