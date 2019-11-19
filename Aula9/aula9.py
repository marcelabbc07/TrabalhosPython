#metodos
from aula9m import soma,sub,mult,div_int,div_fra,resto,raiz
n1=float(input('Digite o primeiro número:'))
n2=float(input('Digite o segundo número:'))
soma=soma(n1,n2)
sub=sub(n1,n2)
mult=mult(n1,n2)
div_int=div_int(n1,n2)
div_fra=div_fra(n1,n2)
resto=resto(n1,n2)
raiz=raiz(n1,n2)
print(f'Soma:{soma}\nSubtração:{sub}\nMultiplicação:{mult}\nDivisão inteira:{div_int}\nDivisão fracionada:{div_fra}\nResto de divisão:{resto}\nRaiz:{raiz:.2f}')
