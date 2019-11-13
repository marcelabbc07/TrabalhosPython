lista_alunos=[]
lista_notas=[]
for i in range(0,10,1):
    lista_alunos.append(input('Digite seu nome:'))
    for i in range(0,1):
        lista_notas.append(float(input('Digite a primeira nota:')))
        lista_notas.append(float(input('Digite a segunda nota:')))
        lista_notas.append(float(input('Digite a terceira nota:')))
        lista_notas.append(float(input('Digite a quarta nota:')))
        media=(lista_notas[0]+lista_notas[1]+lista_notas[2]+lista_notas[3])/4
        for i in lista_alunos:
            print(f'Nome:{[i]}\nMedia:{media}')
            if(media>=7.0):
                print('Aprovado')
            else:
                print('Reprovado')