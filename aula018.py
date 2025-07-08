'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')'''

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
