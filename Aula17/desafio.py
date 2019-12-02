from funcoes import *
menu='''
####################################################################
#               I FESTIVAL DE CERVEJA DE ITUPORÓ                   #
#################################################################### 

1-Cadastro de clientes
2-Ver clientes cadastrados
3-Cadastro de produtos
4-Ver produtos cadastrados
5-Venda de produtos
6-Relatório de vendas
7-Sair

Digite a opção desejada:'''
while True:
    op=input(menu)
    if(op=='1'):
        print('Cadastro de cliente')
    elif(op=='2'):
        print('Ver clientes cadastrados')
    elif(op=='3'):
        print('Cadastro de produtos')
    elif(op=='4'):
        print('Ver produtos cadastrados')
    elif(op=='5'):
        print('Venda de produtos')
    elif(op=='6'):
        print('Relatório de vendas')
    elif(op=='7'):
        print('Sair')
        break
    else:
        print('Digite uma opcão válida') 
        