n1=int(input('Digite o primeiro número:'))
n2=int(input('Digite o segundo número:'))
soma=n1+n2
sub=n1-n2
div=n1/n2
mult=n1*n2
print(f'Soma={soma}\nSubtração={sub}\nDivisão={div}\nMultiplicação={mult}')
if(n1>n2):
    print('O primeiro número digitado é maior')
elif(n1==n2):
    print('Os números são iguais')
else:
    print('O segundo número digitado é maior')