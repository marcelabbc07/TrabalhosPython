lista_alunos=[]
lista_notas=[]
for i in range(0,10):
    lista_alunos.append(input('Digite seu nome:'))
    for x in range(0,10):
        lista_notas.append(float(input('Digite a primeira nota:')))
        lista_notas.append(float(input('Digite a segunda nota:')))
        lista_notas.append(float(input('Digite a terceira nota:')))
        lista_notas.append(float(input('Digite a quarta nota:')))
        media=(lista_notas[x])/4
        if(media>=7.0):
            print('Aprovado')
        else:
            print('Reprovado')
for i in range(0,10):
    print(f'{i}-Nome:{lista_alunos}\nMedia:{media}')
