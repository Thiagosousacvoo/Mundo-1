nome = input('Qual é o seu nome? ')
if nome == 'Thiago':
    print('O meu também é Thiago! Que coincidência!')
elif nome == 'Ana' or 'Maria' or 'Joana':
    print('Que nome bonito!')
else:
    print('Prazer em te conhecer, {}!'.format(nome).title())
