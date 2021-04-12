'''
Faça um programa que leia o nome e a média de um aluno, guardadno tambem a situação em um dicionário.
No final, mostre o conteudo da estrutura na tela.

Nome: Joaquim
Media de Joaquim: 4.5
==========================
Nome é igual a Joaquim
Media é igual a 4.5
Situação é a Igual e reprovado.
'''
aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média do aluno: {aluno["nome"]}:'))
if aluno['media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <=  aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')