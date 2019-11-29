def criar_faixa(mus,alb,art):
    faixa={'musica':mus,'album':alb,'artista':art}
    return faixa
def salvar_faixa(faixa):
    arquivo=open('Aula16/playlist.py','a')
    arquivo.write(f"{faixa['musica']};{faixa['album']};{faixa['artista']}\n")
    arquivo.close()
def ler_faixa():
    arquivo=open('Aula16/playlist.py','r')
    lista_faixas=[]
    for linha in arquivo:
        linha=linha.strip()
        dados_faixa=linha.split(';')
        faixa=criar_faixa(dados_faixa[0],dados_faixa[1],dados_faixa[2])
        lista_faixas.append(faixa)
    arquivo.close()
    return lista_faixas

