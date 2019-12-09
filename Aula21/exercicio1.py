controle='n'
while controle != 's':
    n1=int(input('Digite o primeiro número:'))
    n2=int(input('Digite o segundo número:'))
    print(f'Soma={n1+n2}\nSubtração={n1-n2}\nMultiplicação={n1*n2}\nDivisão={n1/n2}')
    controle=(input("Digite 's' para sair:"))
while True:
    try:
        print('Passou 1')
        n1=int(input('Digite um número:'))
        n2=int(input('Digite um número:'))
        print(n1/n2)
        print('Passou 2')
    except(ValueError,ZeroDivisionError):
        print('Vc digitou o número errado animal!')
    else:
        print('FIM')
        break
