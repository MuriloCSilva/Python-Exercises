import math

rel = int(input('Digite o quantos reais voce possuí: '))

if rel < 5:
    print('Aviso! Com esse dinheiro voce vai conseguir comprar apenas um dólar')

dolar = int(5.01)
dol = rel / dolar

print('O preço do dolar atualmente é: {}'.format(dolar))
print('Com {} voce vai conseguir comprar: {} dolares'.format(rel, dol))