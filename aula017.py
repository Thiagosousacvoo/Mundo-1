'''num = [0, 1, 4, 6, 9 ,10]
print(num)
num[2] = 3
print(num)
num.append(8)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
if 3 in num:
    num.remove(3)
print(num)
num.insert(2, 0)
print(num)
'''

valores = []
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c + 1} encontrei o valore {v}')
print('Final')
    