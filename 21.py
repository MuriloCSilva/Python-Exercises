import random
import os
import sys

print('\033[31m'+'BEM-VINDO AO GAME PEDRA, PAPEL, TESOURA'+'\033[0;0m\n\n')

movimento = int(input('Qual movimento voce deseja realizar?\n'+'\033[33m'+'[1]'+'\033[0;0m'+' Pedra'
      '\n'+'\033[33m'+'[2]'+'\033[0;0m'+' Papel'
      '\n'+'\033[33m'+'[3]'+'\033[0;0m'+' Tesoura\n\n'))

if movimento == 1:
    print('Seu movimento: '+'\033[32m'+'Pedra'+'\033[0;0m')
elif movimento == 2: 
    print('Seu movimento: '+'\033[32m'+'Papel'+'\033[0;0m')
elif movimento == 3:
    print('Seu movimento: '+'\033[32m'+'Tesoura'+'\033[0;0m')
else:
    print('Seu movimento: '+'\033[32m'+'Movimento Inválido!'+'\033[0;0m'); exit()
    


movimentobot = random.randint(1, 3)

if movimentobot == 1:

    print('O bot escolheu o movimento: '+'\033[32m'+'Pedra'+'\033[0;0m')
    if movimento == 1:
        print('EMPATE')
    elif movimento == 2:
        print('\033[32m'+'VOCE VENCEU!'+'\033[0;0m') 
    else:
        print('\033[31m'+'VOCE PERDEU!'+'\033[0;0m')

elif movimentobot == 2:

    print('O bot escolheu o movimento: '+'\033[32m'+'Papel'+'\033[0;0m')
    if movimento == 1:
        print('VOCE PERDEU!')
    elif movimento == 2:
        print('\033[32m'+'EMPATE'+'\033[0;0m') 
    else:
        print('\033[31m'+'VOCE VENCEU!'+'\033[0;0m')

elif movimentobot == 3:

    print('O bot escolheu o movimento: '+'\033[32m'+'Tesoura'+'\033[0;0m')
    if movimento == 1:
        print('VOCE VENCEU!')
    elif movimento == 2:
        print('\033[32m'+'VOCE PERDEU!'+'\033[0;0m') 
    else:
        print('\033[31m'+'EMPATE'+'\033[0;0m')

else:

    print('ERRO!')