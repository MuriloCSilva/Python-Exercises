from datetime import date

maior = 0
menor = 0

for c in range(0,7):
    ano = int(input('Qual o seu ano de nascimento: '))

    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas já são adultas e {} pessoas ainda não atingiram a maioridade.'.format(maior, menor))