def raiz(tipo,n):
    tipo=int(input('Digite o índice de raíz desejado:\n1-Raíz quadrada\n2-Raíz cúbica'))
    n=int(input('Digite um número:'))
    if(tipo==1):
        r=n**1/2
        raiz=r
        print(f'A raíz quadrada de {n} é:{raiz}')
    elif(tipo==2):
        r=n**1/3
        raiz=r
        print(f'A raíz cúbica de {n} é:{raiz}')
    else:
        print('Digite um índice válido')
raiz=raiz(tipo,n)
