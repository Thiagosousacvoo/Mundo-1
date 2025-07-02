preco = float(input('Digite um preço: R$ '))
desconto = preco * 0.05
preco_com_desconto = preco - desconto
print('O preço original é R$ {:.2f}. Com 5% de desconto, o preço é R$ {:.2f}.'.format(preco, preco_com_desconto))