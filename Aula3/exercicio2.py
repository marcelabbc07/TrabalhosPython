nome=(input('Digite seu nome:'))
sobrenome=(input('Digite seu sobrenome:'))
ano=int(input('Digite seu ano de nascimento:'))
print('Seja bem vindo(a) ao Mercado Tech')
if(ano>2001):
    print('1-Produtos não alcóolicos\n2-Sair')
    op=int(input('Selecione a opção desejada:'))
    if(op==1):
        print('Refrigerantes\nSucos\nEnergéticos\nÁguas e chás')
    elif(op==2):
        print('Saindo do Mercado Tech...')
    else:
        print('Selecione uma opção válida')
else:
    print('1-Produtos alcóolicos\n2-Produtos não alcóolicos\n3-Sair')
    op=int(input('Selecione a opção desejada:'))
    if(op==1):
        print('Cervejas\nChopes\nBebidas mistas')
    elif(op==2):
        print('Refrigerantes\nSucos\nEnergéticos\nÁguas e chás')
    elif(op==3):
        print('Saindo do Mercado Tech...')
    else:
        print('Selecione uma opção válida')
        