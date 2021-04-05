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
