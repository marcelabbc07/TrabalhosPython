#manipulação de arquivos
arquivo=open('aula15.txt','a')
arquivo.write('beduschi\n')
arquivo.close

arquivo=open('aula15.txt','r')
for linha in arquivo:
    print(linha)
arquivo.close()

