def porcentagem():
    if(salario<=1000.00):
        cntb=salario*(10/100)
        print(f'Contribuição:{cntb:.2f}\nSalário:{salario-cntb:.2f}')
    elif(salario>=1000.01 and salario<=3000.00):
        cntb= salario*(15/100)
        print(f'Contribuição:{cntb:.2f}\nSalário:{salario-cntb:.2f}')
    elif(salario>=3000.01 and salario<=6000.00):
        cntb=salario*(2/100)
        print(f'Contribuição:{cntb:.2f}\nSalário:{salario-cntb:.2f}')
    elif(salario>=6000.01):
        cntb=salario*(25/100)
        print(f'Contribuição:{cntb:.2f}\nSalário:{salario-cntb:.2f}')
    else:
        print('Valor inválido')
salario=float(input('Digite o seu sálario:'))
porcentagem()