#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação
print('='*50,'\n'*3)
op1='1-Cadastrar funcionário'
op2='2-Listar funcionários'
op3='3-Editar funcionário'
op4='4-Deletar funcionário'
op5='5-Sair'
print('MENU\n{}\n{}\n{}\n{}\n{}'.format(op1,op2,op3,op4,op5))
print('\n'*3,'='*50)