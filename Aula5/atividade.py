nome=str(input('Digite seu nome:'))
idade=int(input('Digite sua idade:'))
if(idade>=18):
    print('O funcionário pode adquirir produtos alcóolicos no Mercado Tech')
else:
    print('O funcionário não pode adquirir produtos alcóolicos no Mercado Tech')
produto=str(input('Digite o nome do produto:'))
categoria=int(input('Digite a categoria do produto:\n1-Alcóolico\n2-Não alcóolico\n'))
if(categoria==1):
    print(produto,'-','Alcóolico')
elif(categoria==2):
    print(produto,'-','Não alcóolico')
else:
    print('Categoria não encontrada')
