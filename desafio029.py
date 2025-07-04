texto = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
num = int(input('Digite um número entre 0 e 10: '))
while num < 0 or num > 10:
    num = int(input('Tente novamente. Digite um número entre 0 e 10: '))
print(f'Você digitou o número {texto[num]}')
