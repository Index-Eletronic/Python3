'''
Faça um programa que insira as palavras numa lista e corrijas.
'''

palavra = []

while True:
    palavra.append(str(input('Digite uma palabra:')))
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in "Nn":
        break
print(palavra)
while True:
    usuario = str(input('Digite a resposta:'))
    for p, a in enumerate(palavra):
        print(f'{p} em {a} tem {palavra}')
