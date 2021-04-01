lanche = 'hamburger', 'suco', 'pizza', 'pudim'
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3]) # Elemento 3 é ignorado
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer comida {comida}')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


