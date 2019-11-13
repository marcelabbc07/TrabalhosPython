#incicialização de uma variável do tipo lista
lista=[]
#inicialização de uma variável lista, com elementos
lista2=['Marcela','Nicole','*Matheus']
#lista de inteiros
lista3=[1,2,3,5]
#lista de tipos diferentes
lista4=[1,'Maykon',12.5]
#impressão das listas criadas
print(lista)
print(lista2)
print(lista3)
print(lista4)
#adicionando elementos em uma lista já criada
lista.append(lista2)
lista.append(lista3)
#impressão das listas modificadas
print(lista)
print(lista2[0])
#criação de lista com dados vindos da função input
lista_perguntas=[input('Digite seu animal favorito:'),input('Digite sua banda favorita:')]
print(lista_perguntas)
#recuperando um dado de uma posição específica da lista
posicao=int(input('Digite a posição:'))
print(lista2[posicao-1])

