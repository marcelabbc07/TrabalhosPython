#--- Exercício 4 - Impressão de dados com a função Print
#--- Imprima textos que simulem a tela inicial de um sistema de compra de bebidas
#--- Nesta tela deve ter um cabeçalho, um menu e um rodapé
#--- O menu deve ter as opções: 
#---   1 - Listar bebidas alcoolicas
#---   2 - Listar bebidas não alcoolicas
#---   3 - Visualizar Pedido
#---   4 - Sair
print('='*50,'\n'*2)
print('MENU\n1-Listar bebidas alcóolicas\n2-Listar bebibas não alcóolicas\n3-Visualizar pedidos\n4-Sair')
op=int(input('Digite a opção desejada:'))
if(op==1):
    print('Cervejas\nChopes\nBebidas mistas')
elif(op==2):
    print('Refrigerantes\nSucos\nEnergéticos\nÁguas e chás')
elif(op==3):
    print('Pedidos:\n')
elif(op==4):
    print('Saindo do Mercado Tech...')
else:
    print('Digite uma opção válida')
print('\n'*2,'='*50)