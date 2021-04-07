'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
 se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expr = str(input('Digite uma expressão')) # Toda string é uma lista. E por usar o FOR para pegar cada letra/simbolo
pilha = []
for simb in expr: # Ira pegar cada simbolo.
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta válida')
else:
    print('Sua expressão está errada.')
