#estruturas de repetição-for
#for simples usando range com incremento padrão de 1
for i in range(0,10):
    print(f'{i}-Padawans HbPy')
#for simples usando range com incremento de 2
for i in range(0,100,2):
    print(f'{i}-Pares')
lista=['Mateus','Matheus','Marcela','Nicole','Tonho','Pablo']
#utilizar for range quando há uma quantidade específica de dados
numero=10
for i in range(0,11):
    print(f'{i}x{numero}={i*numero}')
#for em lista utilizando range
for i in range(0,6):
    print(lista[i])
lista.append('Natan')
#utilizar foreach quando não há uma quantidade específica de dados
for i in lista:
    print(i)

