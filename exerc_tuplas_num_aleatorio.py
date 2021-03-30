'''
 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
  mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

maior = 0
menor = 0
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os numeros soteados foram: ', end= ' ')
for n in num:
    print(f'{n}', end= ' ')

print(f'\nO Maior numero da seguencia é: {max(num)}')
print(f'O Menor numero da seguencia é: {min(num)}')

