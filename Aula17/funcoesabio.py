def cadastrar_cliente(numero):
    dados_cliente=['Código do cliente:','CPF:','Nome completo:','Data de nascimento::','Estado:','Cidade:','CEP:','Bairro:','Rua:','Número:','Complemento:']
    lista=[]
    for j in range(numero):
        dicionario={}
        for i in dados_cliente:
            dicionario[i]=input(f'{i}')
            lista.append(dicionario)
    return lista
def salvar_cliente():
    arquivo=open('Aula17/clientes.txt','a')
    arquivo.write(lista)
    arquivo.close()





# def cadastrar_produto():
#     dados_produto=['Marca:',]
# def venda_produto():
# ncad=int(input('Digite o número de cadastros:'))
# lista_cad=cadastrar_cliente(ncad)