'''
Teoria sobre Dicionários em python
'''

pessoa = {'nome': ' Filipe', 'sexo': 'M', 'idade': 25}
print(pessoa['nome'])
print(pessoa['idade'])
print(f'O{pessoa["nome"]} tem {pessoa["idade"]}') # Como esta dentro de ' ' (simples) tem que colocar "" ( duplas )
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print('-=' * 20)
print('Acessando através de laços.')
for k in pessoa.keys():
    print(k)
print('-=' * 20)
for k, v in pessoa.items():
    print(f'{k} = {v}')
print('-=' * 20)
for k in pessoa.values():
    print(k)
print('-=' * 20)
del pessoa['sexo'] # Ira deletar o elemento sexo.
print(pessoa)
print('-=' * 20)
pessoa['nome']= 'Leandro'  # Modifida o elemento nome.
pessoa['peso']= 98.5 # Adiciona o elemento 'peso'.. NAO precisa utilizar o append.
print(pessoa)
print(f'-=' * 20, {"DICIONARIO DENTRO DE UMA LISTA"}, '-=' * 20)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1) # Uma lista com primeiro elemento.
print(estado2) # Uma lista com segundo elemento.

print(brasil)
print(brasil[0]) # ira mostrar o primeiro elemento
print(brasil[0]['uf']) #Ira mostrar o Rio de Janeiro
print(brasil[1]['Sigla']) # Ira mostra SP
print('-=' * 20)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # .copy substitui o [:]
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    #-- OUUUU
    for v in e.values():
        print(v, end=' ')
    print()# Para pular de linha


