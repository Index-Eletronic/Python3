numeros = list()
while True:
    n = int(input('Digite um valor'))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar.')
    r = str(input('Quer Continuar S/N')).upper().strip()
    if r in "Nn":
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')



