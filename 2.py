import math
n1 = int(input('Digite um número: '))

n2 = (n1 * 2)
n3 = (n1 * 3)
n4 = (math.sqrt(n1))

print('O dobro de {} é: {}'.format(n1, n2))
print('O triplo de {} é: {}'.format(n1, n3))
print('A raiz quadrada de {} é: {:.2f}'.format(n1, n4))