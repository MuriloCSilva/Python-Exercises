import math

salario = int(input('Digite o seu salario: '))
aumento = int(input('Digite o aumento do seu salario em porcentagem: '))

aumentosalario = ((salario * aumento)/100)
salariofinal = (salario + aumentosalario)

print('O aumento no seu salario de {}R$ foi: {}R$'.format(salario, aumentosalario))
print('O seu novo salario é: {}'.format(salariofinal))