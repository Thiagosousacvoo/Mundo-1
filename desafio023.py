valorCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anosPagar = int(input('Em quantos anos você pretende pagar? '))
prestacao = valorCasa / (anosPagar * 12)
limite = salario * 0.3

if prestacao <= limite:
    print('Empréstimo aprovado!')
    print('Valor da prestação: R$ {:.2f}'.format(prestacao))
else:
    print('Empréstimo negado!')
    print('Valor da prestação: R$ {:.2f}'.format(prestacao))
    print('O valor da prestação não pode ser maior que 30% do seu salário.')
    print('Limite de prestação: R$ {:.2f}'.format(limite))

    
