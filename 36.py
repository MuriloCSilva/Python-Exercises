'''
36 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

lista = []

print('Informe 10 números para a lista\n\n')
for n in range(10):
    lista.append(float(input('Digite o '+str(n+1)+'° número da lista: ')))

lista.reverse()
print(lista)