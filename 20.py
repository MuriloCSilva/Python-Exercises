print('\n\033[1m{:=^40}'.format(' Lojinha do seu Zé '))

valor = float(input('\033[32mValor da compra: R$'))

pagamento = int(input(' Forma de pagamento:\n [1] A vista dinheiro\cheque\n [2] A vista no cartão\n [3] Até 2x no cartão\n [4] 3x ou mais no cartão'))

if pagamento == 1:
    valor_final = valor-(valor*10/100)
    print(f'\nSua forma de pagamento é a vista com dinheiro/cheque, você tem 10% de desconto. Portanto o valor que você'
          f' terá que pagar é \033[32mR$ {valor_final:.2f}')

elif pagamento == 2:
    valor_final = valor-(valor*5/100)
    print(f'\nSua forma de pagamento é a vista com cartão, você tem 5% de desconto. Portanto o valor que você terá que '
          f'pagar é \033[32mR$ {valor_final:.2f} ')

elif pagamento == 3:
    print(f'\nSua forma de pagamento é 2x no cartão. O valor que você terá que pagar é \033[32mR$ {valor:.2f}.\n\033[m'
          f'\033[1mMas como vai ser em 2x, você vai ter que pagar \033[32mR$ {valor/2:.2f}\033[m\033[1m em 2 meses')

elif pagamento == 4:

    parcelas = int(input('\nQuantas vezes você vai parcelar? : '))

    if parcelas >= 3:
        valor_final = valor+(valor*20/100)

        print(f'\nSua forma de pagamento é {parcelas}x no cartão, você terá 20% de juros. O valor que você terá que pagar é '
          f'\033[32mR$ {valor_final:.2f}.\n\033[m\033[1mMas como você vai parcelar em {parcelas}x,'
          f' você terá que pagar \033[32mR$ {valor_final/parcelas:.2f}\033[m\033[1m em {parcelas} meses')

    else:
        print('Sua parcela tem que ser igual ou maior que 3 para esta opção.')

else:
    print('Não entendi, tente novamente.')