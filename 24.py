numeros_positivos =  0
numeros_negativos = 0
soma_total = 0
soma_nPositivos = 0
soma_nNegativos = 0
media_nPositivos = 0
media_nNegativos = 0

for contagem in range(1, 41):
    numero = int(input("Digite o número de sua escolha: "))
    soma_total = soma_total + numero

    if numero >= 0:

        numeros_positivos = numeros_positivos + 1
        soma_nPositivos = soma_nPositivos + numero

    else:

        numeros_negativos = numeros_negativos + 1
        soma_nNegativos = soma_nNegativos + numero

media_nPositivos = soma_nPositivos / numeros_positivos
media_nNegativos = soma_nNegativos / numeros_negativos

print('A quantidade de núeros positivos é igual à: '+'\033[32m'+'{}'.format(numeros_positivos)+'\033[0;0m')
print('A quantidade de números negativos é igual à: '+'\033[32m'+'{}'.format(numeros_negativos)+'\033[0;0m')
print('A soma total do números é igual à: '+'\033[32m'+'{}'.format(soma_total)+'\033[0;0m')
print('A soma dos números positivos é igual à: '+'\033[32m'+'{}'.format(soma_nPositivos)+'\033[0;0m')
print('A soma dos números negativos é igual à: '+'\033[32m'+'{}'.format(soma_nNegativos)+'\033[0;0m')
print('A média dos números positivos é igual à: '+'\033[32m'+'{}'.format(media_nPositivos)+'\033[0;0m')
print('A média dos números negativos é igual à: '+'\033[32m'+'{}'.format(media_nNegativos)+'\033[0;0m')