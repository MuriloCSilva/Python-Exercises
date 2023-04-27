n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro valor: '))

if n1 > n2:
    print('O valor {} é maior do que o valor {}'.format(n1, n2))
elif n1 < n2:
    print('O valor {} é menor do que o valor {}'.format(n1, n2))
else:
    print('Os dois valores são iguais')
