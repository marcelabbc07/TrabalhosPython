def menu():
    if(opcao==0):
        print('Usuário realizou o logoff')
    elif(opcao==1):
        print('Cadastro de usuários')
    elif(opcao==2):
        print('Lista de usuários cadastrados')
    else:
        print('Opção invalida.')
opcao=int(input('Selecione a opção desejada:\n0-Sair\n1-Cadastrar\n2-Listar\n'))
menu()