idade = int(input('Insira a sua idade: '))

if idade < 1:
    print('Voce é doido?')
elif idade <= 9:
    print('Voce está na categoria mirin')
elif idade <= 14:
    print('Voce está na categoria infantil')
elif idade <= 19:
    print('Voce está na categoria junior')
elif idade <= 25:
    print('Voce esta na categoria sênior')
else:
    print('Voce está na categoria master')