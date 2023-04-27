'''
35 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

lista = []

print('Informe 5 números para a lista')

for n in range(5):
    lista.append(float(input('Digite o '+str(n+1)+'° número: ')))

print(lista)