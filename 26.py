somasalário = 0
médiasalário = 0
for p in range(1, 16):
    print('--------- {} PESSOA --------'.format(p))
    sexo = str(input('Sexo [M/F]:')).strip()
    salário = float(input('Quanto é seu salário?'))
médiasalário = somasalário / 15
print( ' A media dos salários dos homens e das mulheres são são de {}'.format(médiasalário))