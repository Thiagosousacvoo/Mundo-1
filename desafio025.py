
anos = int(input('Quantos anos você tem? '))
if anos <= 9:
    print('MIRIM')
elif anos <= 14:
    print('INFANTIL')
elif anos <= 19:
    print('JUNIOR')
elif anos <= 25:
    print('SÊNIOR')
else:
    print('MASTER')