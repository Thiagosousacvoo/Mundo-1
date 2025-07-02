"""nome = input('Qual seu nome? ')
if nome == 'Thiago':
    print('O meu também é Thiago! Que coincidência')
else:
    print('Prazer em te conhecer {}!'.format(nome).title())"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('A sua média foi {:.1f}'.format(m))
if m <= 5.0:
    print('Reprovado')
elif m < 7.0:
    print('Recuperação')
else:
    print('Aprovado')



    
