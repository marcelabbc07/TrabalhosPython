# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint
import copy


lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(len(lista1))


# 1.2) Qual é o maior valor da lista2? 
print(max(lista2))


# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
print(max(lista2)+(min(lista2)))


# 1.4) Qual é a média aritmética da lista1?
print(sum(lista1))


# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
print(sum(lista1))
print(sum(lista2))
print(sum(lista3))
print(sum(lista1)+(sum(lista2)+(sum(lista3))))


# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
print(f'')


# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
try:
    print(lista1[5],lista1[9],lista1[10],lista1[25])
    print(lista2[5],lista2[9],lista2[10],lista2[25])
    print(lista3[5],lista3[9],lista3[10],lista3[25])
except(IndexError):
    


# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
if(lista1>lista2 and lista1>lista3):
    print(lista1)
elif(lista2>lista1 and lista2>lista3):
    print(lista2)
elif(lista3>lista1 and lista3>lista2):
    print(lista3)


# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele
print(max(lista1)+(max(lista2)+(max(lista3)-min(lista1)-min(lista2)-min(lista3))))


# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
print(max(lista1)+(max(lista2)+(max(lista3)+min(lista1)+min(lista2)+min(lista3))))

