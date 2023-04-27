s = sm = qe = qc = qa = se = sc = sa = me = mc = ma = xe = xc = xa = 0
print('Digite o seu CÓDIGO e o seu curso e a idade dos 500 alunos. \n'
      'Digite [1] para \033[34mENGENHARIA\033[m '
      '\n[2] para \033[35mCOMPUTAÇÃO\033[m '
      '\n[3] para \033[91mADMINISTRAÇÃO\033[m')
for cont in range(0, 6):
    cod = int(input('\033[36mDigite Seu CÓDIGO:\033[m '))
    id = int(input('\033[91mDigite sua IDADE:\033[m '))

    if cod == 1:
        qe += 1
        se += id
        if id >= 20 and id <= 25:
            xe += 1
    elif cod == 2:
        qc += 1
        sc += id
        mc = sc / qc
        if id >= 20 and id <= 25:
            xc += 1
    elif cod == 3:
        qa += 1
        sa += id
        if id >= 20 and id <= 25:
            xa += 1
    else:
        print('\033[31mCÓDIGO INVÁLIDO\033[m')

me = se / qe
mc = sc / qc
ma = sa / qa

if me < mc and me < ma:
    print('O menor média de idade é a do curso de \033[34mENGENHARIA: \033[m', me)
elif mc < ma and mc < me:
    print('O menor média de idade é a do curso de \033[34mCOMPUTAÇÃO: \033[m', mc)
else:
    print('O menor média de idade é a do curso de \033[34mADMINISTRAÇÃO: \033[m', ma)

print('O numero de alunos no curso de \033[34mENGENHARIA\033[m digitados é de: {}'.format(qe))
print('O numero de alunos no curso de \033[35mCOMPUTAÇÃO\033[m digitados é de: {}'.format(qc))
print('O numero de alunos no curso de \033[91mADMINISTRAÇÃO\033[m digitados é de: {}'.format(qa))
print('O numero de alunos com a idade entre 20 e 25 anos no curso de \033[91mENGENHARIA\033[m digitados é de: {}'.format(xe))
print('O numero de alunos com a idade entre 20 e 25 anos no curso de \033[91mCOMPUTAÇÃO\033[m digitados é de: {}'.format(xc))
print('O numero de alunos com a idade entre 20 e 25 anos no curso de \033[91mADMINISTRAÇÃO\033[m digitados é de: {}'.format(xa))
