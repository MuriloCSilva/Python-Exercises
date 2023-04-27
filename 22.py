from time import sleep

numero = int(input('Digite até que número voce deseja contar: '))
inicio = int(input('Digite a partir de que número voce deseja contar: '))
contagem = int(input('Digite de quantos em quantos números voce deseja contar: '))
print('')

if (inicio < numero):
    cont = inicio
    while cont <= numero:
        print(f'{cont} ', end='', flush=False)
        sleep(0.5)
        cont += contagem
    print('FIM')
else: 
    cont = inicio
    while cont >= numero:
        print(f'{cont} ', end='', flush=False)
        sleep(0.5)
        cont -= contagem
    print('FIM')