# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!
# 1 - Crie um metodo que leia 5 valores inteiros e retorne uma lista.
# Esta função deve ter tratamento de excessão evitando erro ValueError.
# 2 - Com a lista retornada, faça a multiplicação por 5 e salve o resultado
# em outra lista.
# Imprima a lista resultante
def ler_val(n1,n2,n3,n4,n5):
    lista_numeros=[]
    try:
        n1=int(input('Digite o número:'))
        n2=int(input('Digite o número:'))
        n3=int(input('Digite o número:'))
        n4=int(input('Digite o número:'))
        n5=int(input('Digite o número:'))
    except ValueError:
        print('Você digitou o número errado')
    lista_numeros.append(n1)
    lista_numeros.append(n2)
    lista_numeros.append(n3)
    lista_numeros.append(n4)
    lista_numeros.append(n5)
    return lista_numeros
n1=int(input('Digite o número:'))
n2=int(input('Digite o número:'))
n3=int(input('Digite o número:'))
n4=int(input('Digite o número:'))
n5=int(input('Digite o número:'))
lista=ler_val(n1,n2,n3,n4,n5)
lista=lista*5
print(lista)

    