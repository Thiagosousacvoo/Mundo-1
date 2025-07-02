n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print ('O numero {} é maior que o numero {}'.format(n1, n2))
elif n2 > n1:
    print('O numero {} é maior que o numero {}'.format(n2, n1))
elif n1 == n2:
    print('Os números são iguais: {} e {}'.format(n1, n2))
