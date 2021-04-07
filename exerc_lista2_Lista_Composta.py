'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome da pessoa: ')))
    temp.append(int(input('Digite o peso: ')))
    if len(princ) == 0:
        mai = men = temp[1] # se nao gravou nenhum dado vai receber os dados do primeiro.
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp in 'Nn':
            break
print(f'O dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)}')