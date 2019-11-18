#tuplas
numeros=[1,4,6]
usuario={'nome':'user','psswd':123456}
pessoa=('marcela','beduschi',0,45.5,numeros)
numeros[1]=5
usuario['passwd']=456123
print(pessoa[4][1])
lista_pessoas=[]
lista_pessoas.append(pessoa)
pessoa[4][1]=6
print(pessoa[4][1])

