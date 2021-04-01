num = [2, 5, 9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
#num.pop(2)
print(num)
print(f'Essa Lista tem {len(num)} elementos')

#===============================================================
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor|{v}...', end='')
#====================================================================
#ler valores pelo teclado e colocar dentro da lista.

for cont in range(0, 5):
    valores.append(int(input('Digete um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontreio valore {v}')
#====================================================================

a = [2, 3, 4, 7]
b = a[:] # [:] Cria uma cópia de A em B para o python nao mudar as 2 listas caso aja alteração
b[2]=8 # o Python mexe na 2 listas.
print(f'lista A: {a}')
print(f'Lista B: {b}')