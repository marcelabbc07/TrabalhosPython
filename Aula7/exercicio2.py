lista_jogadores=[]
for i in range(0,12):
    dicionario_jogadores={'nome':'','posicao':'','numero':'','pernaboa':''}
    lista_jogadores.append(dicionario_jogadores)
    dicionario_jogadores['nome']=(input('Digite seu nome:'))
    dicionario_jogadores['posicao']=(input('Digite sua posição:'))
    dicionario_jogadores['numero']=int(input('Digite seu número:'))
    dicionario_jogadores['pernaboa']=(input('Digite sua perna boa:'))
print(lista_jogadores)