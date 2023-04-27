import webbrowser;
l1 = int(input('Informe o 1° lado do triângulo: '))
l2 = int(input('Informe o 2° lado do triângulo: '))
l3 = int(input('Informe o 3° lado do triângulo: '))
print('')

if l1 > (l2+l3) or l2 > (l1+l3) or l3 > (l1+l2):
    print('Isso não é um triângulo.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Este é um triângulo isóceles')
    webbrowser.open('https://static.todamateria.com.br/upload/tr/ia/trianguloisosceles3.jpg', new= 1)
elif l1 == l2 == l3:
    print('Este é um triângulo equilatero')
    webbrowser.open('https://static.escolakids.uol.com.br/2020/03/triangulo-equilatero-questao1.jpg', new= 1)
else:
    print('Este é um triângulo escaleno')
    webbrowser.open('https://static.todamateria.com.br/upload/tr/ia/trianguloescalenoexercicio.jpg', new= 1)