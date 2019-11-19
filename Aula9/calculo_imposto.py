def calculo_inss(salario):
    if(salario>=0 and salario<=1751.81):
        inss=salario*(8/100)
    elif(salario>=1751.82 and salario<=2919.72):
        inss=salario*(9/100)
    elif(salario>=2919.73 and salario<=5839.45):
        inss=salario*(11/100)
    else:
        inss=642.3395
    return inss
def calculo_irrf(salario,inss):
    irrf=0
    if(salario>=1903.98 and salario<=2826.55):
        irrf=(((salario-inss)*(7.5/100))-142.80)
    elif(salario>=2826.67 and salario<=3751.05):
        irrf=(((salario-inss)*(15/100))-354.80)
    elif(salario>=3751.06 and salario<=4664.68):
        irrf=(((salario-inss)*(22.5/100))-636.13)
    elif(salario>=4664.69):
        irrf=(((salario-inss)*(27.5/100))-869.36)
    return irrf