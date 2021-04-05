'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or lista[len(lista)-1]: # Se for o primeiro valor
        lista.append(n)
    #elif c > lista[len(lista)-1]: # Para saber se for maior que o ultimo valor, ultimo -1.
        #lista.append(n) - Mesmo comando ( simplificado )
    print(f'Adicionado ao final da lista.')
    else:
       pos = 0
       while pos < len(lista): # Vai verificar se o numero para inserir e menor ou igual a ele.
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em Ordem foram {lista}')
