lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')


for cont in range(0, len(lanche)):
    print(f'{cont} Eu vou comer {lanche[cont]}')
print('Fim')


for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')


for pos, comida in enumerate(lanche):
    print(f'{pos} Eu vou comer {comida}')
