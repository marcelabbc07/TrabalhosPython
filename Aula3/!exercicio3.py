nome=(input('Digite seu nome completo:'))
cpf=int(input('Digite seu CPF:'))
rg=int(input('Digite seu RG:'))
cargo=(input('Digite seu cargo:'))
salario=float(input('Digite seu salário:'))
#--- INSS -  de    0,00 ate 1751,81 - percetual =  8,0%
#---         de 1751,82 ate 2919,72 - percetual =  9,5%
#---         de 2919,72 ate 5839,45 - percetual = 11,0%
#--- Deve ser calculado o valor do IRRF - 
#---         de 2826,66 ate 3751,05 - percetual = 15,0%
#---         de 3751,06 ate 4664,68 - percetual = 22,5%
#---         de 4664,69 ate ------- - percetual = 27,5%
if(salario>=0 and salario<=1751.81):
    inss=salario*(8/100)
    salario_final=salario-inss
    print(salario_final)
elif(salario>=1751.82 and salario<=2919.72):
    inss=salario*(9.5/100)
    salario_final=salario-inss
    print(salario_final)
    if(salario>=1903.98 and salario<=2826.55):
        irrf=salario*(7.5/100)
        inss=salario*(9.5/100)
        salario_final=salario-irrf-inss
        print(salario_final)
elif(salario>=2919.73 and salario>=5839.45):
    inss=salario*(11/100)
    salario_final=salario-inss
    print(salario_final)
elif(salario>=2826.67 and salario<=3751.05):
    
