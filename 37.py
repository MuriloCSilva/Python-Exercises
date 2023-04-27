'''
37 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

import sys
from colorama import Fore, Back, Style

notas = []

for n in range(4):
    notas.append(float(input('Digite a nota do '+str(n+1)+'° bimestre: ')))

media = (notas[0]+notas[1]+notas[2]+notas[3])/4


print('\n\n')
print('-'*20)
print('Notas:')
print(notas)
print('-'*20)
print('Média Final: ')
print(media)
print('-'*20)

if (media < 6):
    print(Fore.RED+'ALUNO REPROVADO!')
elif (media >= 6):
    print(Fore.GREEN+'ALUNO APROVADO!')
else:
    print('Erro, algo deu errado!')
    sys.exit()