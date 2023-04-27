Ssal = Msal = Qcemsal = QF = QM = POmn = POma = Qsal = Qid = sex = highage = 0
lowage = 999999
hab = int(input('Digite a quantidade de \033[34mHABITANTES\033[m da cidade: '))
for cont in range(0, hab):
    id = int(input('Digite Sua \033[36mIDADE\033[m: '))
    Qid += 1
    if id > highage:
        highage = id
        POma = Qid
    if id < lowage:
        lowage = id
        POmn = Qid
    if id < 0:
        print('\033[31mCONTAGEM ENCERRADA: IDADE INVÁLIDA\033[m')
        break
    sex = str(input('Digite Seu \033[31mSEXO\033[m (\033[36mM\033[m/\033[35mF\033[m): '))
    if sex == 'F':
        QF += 1
    else:
        QM += 1
    sal = float(input('Digite seu \033[33mSÁLARIO\033[m: '))
    Ssal += sal
    Qsal += 1
    Msal = Ssal / Qsal
    if sal < 0:
        print('\033[31mCONTAGEM ENCERRADA SÁLARIO INVÁLIDO!\033[m')

    if sal <= 100:
        Qcemsal += 1
print('A média de Sálario do grupo foi de: {:.2f}'.format(Msal))
print('A \033[32mMAIOR\033[m \033[36mIDADE\033[m do grupo é a \033[33m{}° Pessoa com {} anos\033[m'. format(POma, highage))
print('A \033[31mMENOR\033[m \033[36mIDADE\033[m do grupo é a \033[33m{}° Pessoa com {} anos\033[m'.format(POmn, lowage))
print('A Quantidade de mulheres com sálario até \033[32mR$100\033[m do grupo foi de: {:.2f}'.format(Qcemsal))