numeros = 0
for num in  range(1, 51):

    if num % 3 == 0:
        numeros = numeros + 1
    
print('Entre os '+'\033[32m'+'50'+'\033[0;0m'+' números, \033[32m'+'{}'.format(numeros)+'\033[0;0m'+' são divisiveis por 3')
