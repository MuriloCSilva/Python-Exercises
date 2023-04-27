'''
38 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

import re

lista = []
contvogal = 0
vogais = ['aeiou']
contconsoante = 0
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

print('Digite 10 caracteres separadamente\n\n')
for n in range(10):
    newcaract = lista.append(str(input('Digite o '+str(n+1)+'° caractere da lista: ')).lower())

    if newcaract in vogais:
        contvogal += 1
    if newcaract in consoantes:
        contconsoante += 1

contvogal = str(contvogal)
contconsoante = str(contconsoante)
lista = ''.join(c for c in lista if c not in 'aeiou')
voga = ''.join(c for c in lista if c not in 'bcdfghjklmnpqrstvwxyz')
print('-'*20)
print('Consoantes: '+lista)
print('Total de consoantes: '+contconsoante)
print('-'*20)
print('Vogais: '+voga)
print('Total de vogais: '+contvogal)
print('-'*20)