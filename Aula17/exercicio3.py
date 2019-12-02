from random import randint
rand=randint(1,10)
n=0
while(not n==rand):
    n=int(input('Digite um número:'))
    if(n==rand):
        print('Você acertou')
    elif(n<rand):
        print('O número digitado é menor')
    elif(n>rand):
        print('O número digitado é maior')
    elif(n<0 and n>10):
        print('Digite um número válido')

