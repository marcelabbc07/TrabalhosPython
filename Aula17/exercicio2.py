menu='''
                      MENU

1-Cadastro da banda
2-Cadastro do álbum
3-Cadastro da música
4-Sair

Digite a opçaõ desejada:'''
lista_b=[]
lista_a=[]
lista_m=[]
while True:
    op=input(menu)
    if(op=='1'):
        print('Cadastro da banda')
        lista_b.append(input('Digite o nome da banda:'))
    elif(op=='2'):
        print('Cadastro do álbum')
        lista_a.append(input('Digite o nome do álbum:'))
    elif(op=='3'):
        print('Cadastro da música')
        lista_,.append(input('Digite o nome da música:'))
    elif(op=='4'):
        print(f'Banda:{}')
    else:
        print('Digite uma opçaõ válida')