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

    