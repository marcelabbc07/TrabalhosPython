#web2
from calculo_imposto import calculo_inss,calculo_irrf
salario=float(input('Digite seu salário:'))
inss=calculo_inss(salario)
irrf=calculo_irrf(salario,inss)
salario_final=salario-inss-irrf
print(f'INSS:{inss:.2f}\nIRRF:{irrf:.2f}\nSeu salário líquido é:{salario_final:.2f}') 