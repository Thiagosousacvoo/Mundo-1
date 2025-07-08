def dobrar(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao]*= 2
        posicao += 1



valores=[7, 2, 5, 0, 4]
dobrar(valores)
print(valores) 