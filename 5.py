import math

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))

if n1 < n2 and n3:
    n4 = (n1 * n2) * n3 
    print('O produto de {}, {} e {} é: {}'.format(n1, n2, n3, n4))

if n2 < n1 and n3:
    n4 = (n2 * n1)* n3
    print('O produto de {}, {} e {} é: {}'.format(n1, n2, n3, n4))

if n3 < n1 and n3:
    n4 = (n3 * n1)* n2
    print('O produto de {}, {} e {} é: {}'.format(n1, n2, n3, n4))