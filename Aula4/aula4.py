#atribuição de tipo em uma variável
n1=float(input('Digite o primeiro número:'))
n2=float(input('Digite o segundo número:'))
soma=n1+n2
sub=n1-n2
div=n1/n2
mult=n1*n2
print(f'Soma={soma}\nSubtração={sub}\nDivisão={div}\nMultiplicação={mult}')
#estrutura de decisão
#caso a condição validada no if seja falsa, é validada a condição do elif, caso a condição do elif seja falsa, else é executado
if(n1>n2):
    print('O primeiro número digitado é maior')
elif(n1==n2):
    print('Os números são iguais')
else:
    print('O segundo número digitado é maior')