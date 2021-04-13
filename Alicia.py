'''
Faça um programa que insira as palavras numa lista e diga se estão corretas..
'''
import random
from time import sleep

print('-=' * 10, "\33[0;33;44mBEM VINDO A PROFa.ALICIA V1.0\33[m", '-=' * 10 )
print()
print('O QUE VOCÊ GOSTARIA DE ESTUDAR HOJE?')
print('ESCOLHA A OPÇÃO:')
print('''        [1] - EXERCICÍOS DE PORTUGUÊS
        [2] - EXERCÍCIOS DE MATEMÁTICA
        [3] - EXERCÍCIOS DE GEOGRÁFIA
        [4] - SAIR DO PROGRAMA''')
opcao = conta = conte = 0
while opcao != 4:
    opcao = int(input(' Digite a opção que deseja:'))
    if opcao == 1:
        print('BEM VINDO A AULA DE PORTUGUÊS !')
        sleep(2)
        print('OBJETIVO: ADIVINHE SE A PALABRA SORTEADA TEM "S", "SS", "C" OU "Ç".')
        sleep(2)
        palavra = random.choice(['acessível', 'agressivo', 'assim', 'assinar']).strip().upper()
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
        print('BEM VINDO A AULA DE MATEMÁTICA !')

    elif opcao == 3:
        print('BEM VINDO A AULA DE GEOGRÁFIA')

    else:
        break





'''
select = random.choice(['acessível', 'agressivo', 'assim','assinar']).strip().upper()
S = "SS"
print(select)
#for palavra in range(0, len(select)):
 #       select = select.replace()

original = "EXAMPLE"
removed = original.replace("M", "")
print(removed)
'''