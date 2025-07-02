salario = float(input('Digite seu salario: R$ '))
aumento = salario * 0.15
salario_com_aumento = salario + aumento
print('O salario original é R$ {:.2f}. Com 15% de aumento, o salario fica R$ {:.2f}.'.format(salario, salario_com_aumento))