carteira = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = 5.50
real = carteira / dolar
print('Com R$ {:.2f} você pode comprar US$ {:.2f} dólares'.format(carteira, real))
