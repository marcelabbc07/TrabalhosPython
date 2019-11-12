nome=(input('Digite seu nome:'))
idade=int(input('Digite sua idade:'))
if(idade>=18):
    print('O funcionário pode adquirir produtos alcóolicos no Mercado Tech')
else:
    print('O funcionário não pode adquirir produtos alcóolicos no Mercado Tech')
produto=(input('Digite o nome do produto:'))
categoria=(input('Digite a categoria do produto:\nAlcóolico\nNão alcóolico\n'))
print(produto,'-',categoria)
if(idade<18 and categoria=='Alcóolico'):
    print('Seleciona outro produto')