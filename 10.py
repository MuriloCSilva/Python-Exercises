vel = int(input('Digite a sua velicidade: '))

if vel > 80:
    print('Voce estava acima de 80Kk/h, e por isso voce foi multado')
    multa = (vel - 80) * 7
    print('Valor da multa: {}'.format(multa))
else:
    print('Voce não estava acima de 80Km/h, continue sua viagem')