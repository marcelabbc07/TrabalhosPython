def salvar(cervejas_funcao):
    arquivo=open('cervejas.txt','a')
    arquivo.write(f"{cervejas_funcao['marca']};{cervejas_funcao['tipo']};{cervejas_funcao['teor']}\n")
    arquivo.close
def ler():
    lista=[]
    arquivo=open('cervejas.txt','r')
    for linha in arquivo:
        linha=linha.strip()
        lista_linha=linha.split(';')
        cervejas={'marca':lista_linha[0],'tipo':lista_linha[1],'teor':lista_linha[2]}
        lista.append(cervejas)
    arquivo.close()
    return lista
marca=input('Digite a marca da cerveja:')
tipo=input('Digite o tipo da cerveja:')
teor=(input('Digite o teor alcóolico da cerveja:'))
cervejas={'marca':marca,'tipo':tipo,'teor':teor}
salvar(cervejas)
for i in ler():
    print(f"{i['marca']} - {i['tipo']} - {i['teor']}")