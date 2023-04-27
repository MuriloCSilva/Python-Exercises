primeiro = int(input('primeiro termo:'))
razão = int(input('Razão:'))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=',')
print('ACABOU')
