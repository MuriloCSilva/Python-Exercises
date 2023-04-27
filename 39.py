'''
39 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

lista = []
par = []
impar = []

for n in range(20):
    lista.append(int(input('Digite o '+str(n+1)+'° número: ')))

for n in range(20):
    if lista[n] % 2 == 0:
        par.append(lista[n])
    else:
        impar.append(lista[n])

print('Lista do números: '+str(lista))
print('Lista números pares: '+str(par))
print('Lista números impares: '+str(impar))