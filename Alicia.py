'''
Faça um programa que insira as palavras numa lista e diga se estão corretas..
'''
import random
from random import randint
from time import sleep

print('-=' * 10, "\33[0;40;42mBEM VINDO A PROFa.ALICIA V1.0\33[m", '-=' * 10 )
print()
print('O QUE VOCÊ GOSTARIA DE ESTUDAR HOJE?')
print('ESCOLHA A OPÇÃO:')
print('''        [1] - EXERCICÍOS DE PORTUGUÊS
        [2] - EXERCÍCIOS DE MATEMÁTICA
        [3] - EXERCÍCIOS DE GEOGRÁFIA
        [4] - SAIR DO PROGRAMA''')
opcao = int(input(' Digite a opção que deseja:'))
conta = conte = 0
n1 = 0
n2 = 0
if opcao == 1:
    print('BEM VINDO A AULA DE PORTUGUÊS !')
    sleep(2)
    print('OBJETIVO: ADIVINHE SE A PALABRA SORTEADA TEM "S", "SS", "C" OU "Ç".')
    sleep(2)
elif opcao == 2:
    print('BEM VINDO A AULA DE MATEMÁTICA !')
    sleep(2)
    print('OBJETIVO: FAÇA AS CONTAS A SEGUIR.')
    sleep(2)
elif opcao == 3:
    print('BEM VINDO A AULA DE GEOGRÁFIA')

elif opcao == 4:
    print('SAINDO DO PROGRAMA')
    sleep(3)

while opcao != 4:
    if opcao == 1:
        palavra = random.choice(
            ['acetinado', 'açafrão', 'almaço', 'anoitecer', 'censura', 'cimento', 'dança', 'contorção',
             'exceção', 'endereço', 'Iguaçu', 'maçarico', 'maçaroca', 'maço', 'maciço', 'miçanga',
             'muçulmano', 'paçoca',
             'pança', 'pinça', 'Suíça', 'ânsia', 'ansiar', 'ansioso', 'ansiedade', 'cansar', 'cansado',
             'descansar', 'descanso',
             'diversão', 'excursão', 'farsa', 'ganso', 'hortênsia', 'pretensão', 'pretensioso',
             'propensão', 'remorso', 'sebo', 'tenso', 'utensílio', 'acesso', 'acessório', 'acessível',
             'assar', 'asseio', 'assinar',
             'carrossel', 'cassino', 'concessão', 'discussão', 'escassez', 'escasso', 'essencial',
             'expressão', 'fracasso', 'impressão', 'massa',
             'massagista', 'missão', 'necessário', 'obsessão', 'opressão', 'pêssego', 'procissão',
             'profissão', 'ressurreição', 'sessenta',
             'sossegar', 'sossego', 'submissão', 'sucessivo']).strip().upper()
        if 'S' in palavra:
            sems = palavra.replace("S", "")
        elif 'SS' in palavra:
            sems = palavra.replace("SS", "")
        elif 'C' in palavra:
            sems = palavra.replace("C", "")
        elif 'Ç' in palavra:
            sems =palavra.replace("Ç", "")

        print(f'A PALABRA SORTEADA É: {sems}')
        resp = str(input('DIGITE A PALABRA CORRETA AQUI: ')).strip().upper()

        if resp == palavra:
            print('VOCÊ ACERTOU, PARABENS')
            conta += 1
        else:
            print('VOCE ERROU !')
            conte += 1
        pergunta = ' '
        while pergunta not in 'SN':
            pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
            if pergunta == 'N':
                break

    elif opcao == 2:
        n1 = randint(0, 100)
        n2 = randint(0, 100)
        sub = n1 - n2
        div = n1 - n2
        escolha = random.choice(['SOMA', 'SUBTRAÇÂO', 'DIVISÂO'])
        sleep(2)
        print(f' === O COMPUTADOR ESCOLHEU 2 NUMEROS ->:', end=' ')
        sleep(2)
        print(f'{n1}', end=' ')
        sleep(2)
        print( ' E ', end=' ')
        sleep(2)
        print(f'{n2}')
        result = float(input(f'Qual o resultado da {escolha} entre eles: '))
        if escolha[0]:
                soma = n1 + n2
                result = soma
                if result == soma:
                    print('Voce acertou!')
                else:
                    print(f'O resultado correto é: {soma}')
                    print('Voce errou!')

    elif opcao == 3:
        print('BEM VINDO A AULA DE GEOGRÁFIA')

    else:
        break
