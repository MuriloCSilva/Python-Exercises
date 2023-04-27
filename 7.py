import math

alt = int(input('Digite qual é a altura da parede em metros: '))
lar = int(input('Digite qual é a largura da parede em metros: '))

area = alt * lar
tinta = int(2.3)
tin = area / tinta

print('A quantidade de tinta para pitnar uma parede com uma área de {} é: {} litros de tinta'.format(area, tin))