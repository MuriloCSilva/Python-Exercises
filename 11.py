km = int(input('Digite a distância de sua viagem em quilometros: '))

if km < 200:
    val = km * 0.50
    print('A sua viagem é menor que 200Km, por isso serão cobrados 0,50R$ por Km. O valor da sua viagem é: {}'.format(val))
else:
    vall = km * 0.45
    print('A sua viagem é maior que 200Km, por isso serão cobrados 0,45R$ por Km. O valor da sua viagem é: {}'.format(vall))