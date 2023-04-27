valor = int(input('Qual é o valor da casa? '))
sal   = int(input('Qual o valor do seu salário? '))
an    = int(input('Em quantos anos voce pretende pagar a casa? '))

meses = an * 12
parce = valor / meses
min = (sal/100) * 30

if parce < min:
    print('O seu empréstimo foi aprovado!')
else:
    print('O seu empréstimo foi negado.')