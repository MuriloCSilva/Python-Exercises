import math

print('')
preço    = int(input('Digite o preço do produto: '))
desconto = int(input('Digite o desconto do produto: '))
vd       = ((preço * desconto)/100)
vf       = (preço - vd)

print('O valor descontado do produto de {}R$ é: {}R$'.format(preço, vd))
print('O valor final do produto é: {}R$'.format(vf))