'''
Exemplos da explicação
'''

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # [:] faz uma cópia da estruta para nao alterar a outra
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
#===================================================================================================
        #--Estrutura 0   Estrutura 1   Estrutura 2      Estrutura 3
galera = [['Joao, 19'], ['Ana', 33], ['Joaoquim', 13], ['Maria', 45]]
print([0])
print([0][0])
for p in galera:
    print(p)
    print([0])
    print([1])
    print(f'{p[0]} tem {p[1]} anos de idade')
#===================================================================================================

galera = list()
dado = list()
totmai = totmeno = 0
for c in range(0, 3):
    dado.append(str(input('NOME: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # [:] Faz a copia dos dados.
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é Maior de Idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmeno += 1
print(f'Tenmos {totmai} maiores de idade e {totmeno} menores de idade')