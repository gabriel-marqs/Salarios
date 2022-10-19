print('\033[1;30;42m\nDESCUBRA SEU SALÁRIO LÍQUIDO \033[m')
sal = float(input('\nInforme o salário atual: R$ ').replace(",", "."))
teto1 = float(1212)
descmax1 = teto1 * 0.075
teto2 = float(2427.35)
descmax2 = (teto2 - teto1) * 0.09
teto3 = float(3641.03)
descmax3 = (teto3 - teto2) * 0.12
teto4 = float(7087.22)
descmax4 = (teto4 - teto3) * 0.14
descvt = float(0)
descir = float(0)
if sal <= teto1:
    desc1 = sal * 0.075
    res = desc1
elif teto1 < sal <= teto2:
    rest = sal - teto1
    desc2 = rest - (rest - (rest * 9 / 100))
    res = descmax1 + desc2
elif teto2 < sal <= teto3:
    rest2 = sal - teto2
    desc3 = rest2 - (rest2 - (rest2 * 12 / 100))
    res = descmax1 + descmax2 + desc3
elif teto3 < sal <= teto4:
    rest3 = sal - teto3
    desc4 = rest3 - (rest3 - (rest3 * 14 / 100))
    res = descmax1 + descmax2 + descmax3 + desc4
else:
    res = descmax1 + descmax2 + descmax3 + descmax4
rvt = input(str('\nVocê utiliza vale transporte? (S/N): '))

if rvt.lower()[0] == str('s'):
    cvt = input('\nSabe confirmar o valor recebido do vale transporte? (S/N): ')
    if cvt.lower()[0] == 's':
        vt = input('\nInforme o valor recebido como Vale Transporte: R$ ').replace(",", ".")
        vt = float(vt)
        dvt = sal * 0.06
        if dvt < vt:
            descvt = dvt
        else:
            descvt = vt
    elif cvt.lower()[0] == 'n':
        descvt = sal * 0.06
        print('\nO desconto de vale transporte equivale a 6% do salário bruto.\n'
              'Caso o desconto seja superior ao valor recebido, será descontado o valor recebido em sua totalidade\n'
              'Para uma informação mais precisa, sugerimos consultar o valor recebido de vale transporte.\n')
    else:
        print('\nPreenchimento incorreto, tente novamente.\n')
        exit()
elif rvt.lower()[0] == 'n':
    descvt = 0
    print('\nNão será contabilizado desconto de vale transporte\n')
else:
    print('\nErro de preenchimento, verifique as informações e tente novamente.\n')
    exit()
if sal < 1903.99:
    descir = 0
elif 1903.99 <= sal <= 2826.65:
    descir = 142.8
elif 2826.66 <= sal <= 3751.05:
    descir = 354.8
elif 3751.06 <= sal <= 4664.68:
    descir = 636.13
else:
    descir = 869.36

ns = sal - res - descvt - descir

print('------------------------------------------------------------------------------------------')
print('\nSalário Bruto:                     R$ {:.2f}\n'
      '\nDesconto INSS:                     R$ {:.2f}\n'
      '\nDesconto VALE TRANSPORTE:          R$ {:.2f}\n'
      '\nDesconto IMPOSTO DE RENDA:         R$ {:.2f}\n'
      '\nSalário Líquido:                   R$ {:.2f}\n'.format(sal, res, descvt, descir, ns).replace(".", ",").upper())
print('------------------------------------------------------------------------------------------')