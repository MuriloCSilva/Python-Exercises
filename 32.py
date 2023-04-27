# 32- Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
n1 = int(input('Escreva um número: '))
tot = 0
for c in range(1, n1 +1):
    if n1 % c == 0:
     print('\033[34m', end='')
     tot += 1
    else:
     print('\033[31m', end='')
    print('{} '.format(c), end='')
print('O número {} foi divisivel {} vezes'.format(n1, tot))