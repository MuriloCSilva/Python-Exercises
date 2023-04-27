maior = 0
menor = 9999
for p in range(1, 91):
    print('--------- {} BOI --------'.format(p))
    codigo = float(input('codigo do BOI:'))
    peso = float(input('Peso do boi:'))
    if peso > maior:
        maior = peso
        cod = codigo
    if peso < menor:
        menor = peso
        cod2 = codigo
print('\033[32m O Boi pesado tem {} kg. Codígo do é boi é {} \033[m.'.format(maior, cod))
print('\033[31m O Boi magro  tem {} kg. Codígo do é boi é {} \033[m.'.format(menor, cod2))