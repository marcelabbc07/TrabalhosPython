lista_alunos=[]
lista_notas=[]
n1=0
n2=1
n3=2
n4=3
for i in range(0,10,1):
    lista_alunos.append(str(input('Digite seu nome:')))
    for i in range(0,1,1):
        lista_notas.append(float(input('Digite a primeira nota:')))
        lista_notas.append(float(input('Digite a segunda nota:')))
        lista_notas.append(float(input('Digite a terceira nota:')))
        lista_notas.append(float(input('Digite a quarta nota:')))
for i in lista_alunos:
    media=(lista_notas[n1]+lista_notas[n2]+lista_notas[n3]+lista_notas[n4])/4
    print(f'Nome:{[i]}\nMedia:{media}')
    if(media>=7.0):
        print('Aprovado')
    else:
        print('Reprovado')
    n1+=4
    n2+=4
    n3+=4
    n4+=4