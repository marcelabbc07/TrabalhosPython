def exportar_txt(lista_pessoa):
    #Cria um arquivo e atribui a uma variável 'arquivo'
    with open('Aula33/pessoas.txt','a') as arquivo:
    #Percorre a ista de dicionário e salva no arquivo em formato pré-definido
        for p in lista_pessoa:
            arquivo.write(f"{p['id']};{p['nome']};{p['sobrenome']};{p['idade']};{p['endereco_id']}\n")
            print(f'\t{p}')
