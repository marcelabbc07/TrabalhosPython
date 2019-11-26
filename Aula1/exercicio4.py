print('='*50,'\n'*2)
print('MENU\n1-Listar bebidas alcóolicas\n2-Listar bebibas não alcóolicas\n3-Visualizar pedidos\n4-Sair')
op=int(input('Digite a opção desejada:'))
if(op==1):
    print('Cervejas\nChopes\nBebidas mistas')
elif(op==2):
    print('Refrigerantes\nSucos\nEnergéticos\nÁguas e chás')
elif(op==3):
    print('Pedidos')
elif(op==4):
    print('Saindo do Mercado Tech...')
else:
    print('Digite uma opção válida')
print('\n'*2,'='*50)

