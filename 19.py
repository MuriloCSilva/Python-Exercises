altura = float(input('Insira a sua altura em metros: '))
peso = float(input('Insira o seu peso em Kg: '))

imc = peso / (altura*2)
print('O seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Voce está abaixo do peso ideal')
elif imc >= 18.5 and imc <= 25:
    print('Voce está no peso ideal')
elif imc > 25 and imc <= 30:
    print('Voce está com sobrepeso')
elif imc > 30 and imc <= 40:
    print('Voce esta com obesidade')
else:
    print('Voce está com obesidade mórbida')