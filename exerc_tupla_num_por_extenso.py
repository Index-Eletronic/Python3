'''
Crie um programa que tenha uma tupla totalmente preenchida com um contagem por extenso de zero ate vinte.
Seu programa devera ler um numero pelo teclado entre 0 e 10  e mostralo por extenso.
'''


cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove','dez')
res = 'S'
while True:
    if res == 'S':
        n = int(input('Digite um numero entre 0 e 10: '))
        if 0 <= n <= 10:
            break
        print('Tente novamente...', end=' ')
    print(f'Você digitou o numero: {cont[n]}.', end= ' ')
    print('Vocẽ que continuar? [S / N]')
