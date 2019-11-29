def salvar(pessoa):
    arquivo=open('Aula15/dados.txt','a')
    arquivo.write(f"{pessoa['nome']};{pessoa['sobrenome']};{pessoa['idade']}\n")
    arquivo.close()
def ler():
    lista=[]
    arquivo=open('Aula15/dados.txt','r')
    for linha in arquivo:
        linha=linha.strip()
        lista_linha=linha.split(';')
        pessoa={'nome':lista_linha[0],'sobrenome':lista_linha[1],'idade':lista_linha[2]}
        lista.append(pessoa)
    arquivo.close()
    return lista
nome=input('Digite seu nome:')
sobrenome=input('Digite seu sobrenome:')
idade=int(input('Digite sua idade:'))
pessoa={'nome':nome,'sobrenome':sobrenome,'idade':idade}
salvar(pessoa)
for i in ler():
    print(f"{i['nome']} - {i['sobrenome']} - {i['idade']}")


