sal = int(input('Digite o seu salário: '))

if(sal <= 1250):
    aum = 15
else:
    aum = 10

aume = aum/100
aumento = aume * sal
ns = sal + aumento

print('O aumento percentual de {}%, com um aumento de {}, resultando no novo salário de: {}'.format(aum, aumento, ns))
