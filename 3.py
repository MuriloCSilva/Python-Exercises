import math

print('-------------------------------------------')
print('Ola! Bem-vindo a calculadora de média final')
print('-------------------------------------------')
n1 = int(input('Digite a média do 1° bimestre: '))
n2 = int(input('Digite a média do 2° bimestre: '))
n3 = int(input('Digite a média do 3° bimestre: '))
n4 = int(input('Digite a média do 4° bimestre: '))
n5 = (n1 + n2 + n3 + n4) / 4
print('-------------------------------------------')
print('A média final do aluno foi: {}'.format(n5))
print('-------------------------------------------')
if n5 <= 5: print('Aluno reprovado!')
else: print('Aluno Aprovado!')