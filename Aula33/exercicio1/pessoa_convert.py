def converter_tabela_classe(lista_tuplas):
#Cria uma lista para armazenar dicionários
    lista_pessoa=[]
#Pega cada posição da tupla e atribui a uma chave do dicionário
    for p in lista_tuplas:
        dict_pessoa={'id':0,'nome':'','sobrenome':'','idade':0,'endereco_id':0}
        dict_pessoa['id']=p[0]
        dict_pessoa['nome']=p[1]
        dict_pessoa['sobrenome']=p[2]
        dict_pessoa['idade']=p[3]
        dict_pessoa['endereco_id']=p[4]
        lista_pessoa.append(dict_pessoa)
    return lista_pessoa
