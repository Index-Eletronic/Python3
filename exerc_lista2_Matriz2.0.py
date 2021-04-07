'''
 Aprimore o desafio anterior (Matriz), mostrando no final:
 A) A soma de todos os valores pares digitados.
 B) A soma dos valores da terceira coluna.
 C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A) A Soma dos numeros pares é: {spar}')
for l in range (0, 3):
    scol += matriz[l][2] # A Coluna e sempre fixa e a linha é variavel
print(f'A soma dos valores da terceira coluna é: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O Maior valor da segunda linha é: {mai}')

