texto = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Tente novamente. Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        break
print(f'Você digitou o número {texto[num]}')


