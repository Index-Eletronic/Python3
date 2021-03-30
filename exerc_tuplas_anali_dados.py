'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
num = (int(input('Digite um numero: ')),
       int(input('Digite Outro numero:')),
       int(input('Digite Mais um numero:')),
       int(input('Digite o Ultimo numero:')))

print(f'Voce digitou os valores: {num}')
print(f'O Valor 9 apareceu {num.count(9)} vezes')
if 3 in  num:
    print(f'O valor 3 apareceu {num.count(3)+1} posição')
else:
    print('O Valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')
