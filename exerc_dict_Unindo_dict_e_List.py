'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

galera = list()  # Para guardar um dicionario ( varias pessoas ) dentro de uma lista.
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear() # Limpa os dados para receber uma pessoa nova.
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo [M / F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
                break
        print('ERRO! Por Favor digite M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input(' Quer Continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S OU N')
    if resp == 'N':
        break
print('-=' * 30)
# Para Mostrar quantas pessoas temos cadastradas:
print(f'A- ) No Total temos {len(galera)} pesoosas Cadastradas')
media = soma / len(galera)
print(f'B- ) A Média de idade é de {media:5.2f} anos.')
print(f'C- )  As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D- ) A Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('  ')
        for k,  v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<<ENCERRADO>>')


