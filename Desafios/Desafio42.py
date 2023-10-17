dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))

if mes in (1, 2):
   print('verão')
elif mes == 3:
    if dia < 21:
        print('verão')
    else:
        print ('outono')
elif mes in (4, 5):
    print ('outono')
elif mes == 6:
    if dia < 21:
        print('outono')
    else:
        print('Inverno')
elif mes in (7, 8):
    print ('inverno')
elif mes == 9:
        if dia < 21:
            print ('inverno')
else:
    print ('primavera')
    if mes in (10, 11):
        print ('primavera')
    elif mes == 12:
        if dia < 21:
            print('primavera')
    else:
            print('primavera')
