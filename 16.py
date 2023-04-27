nas = int(input('Insira o seu ano de nascimento: '))
idade = 2021 - nas
if nas < 1980:
    print('Insira um valor válido')
    import sys
    sys.exit()

if idade < 18:
    tempo = 18 - idade
    print('Ainda falta {} anos para voce se alistar.'.format(tempo))
elif idade == 18:
    print('Voce possuí 18 anos, portanto voce deve se alistar.')
else:
    tempo = idade - 18
    print('Voce ja passou {} anos do tempo de se alistar.'.format(tempo))