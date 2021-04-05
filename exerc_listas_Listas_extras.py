'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

num = list()
pares = list()
impares = list  ()
while True:
    num.append(int(input('Digite um numero:')))
    resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A Lista completa é: {num}')
print(f'A lista de numeros pares são: {pares}')
print(f'A lista de numeros imapares são: {impares}')