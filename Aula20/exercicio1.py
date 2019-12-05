# Aula 20 - 05-12-2019
# Lista com for e metodos
# Com esta lista:
# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com biblioteca.
# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.
#
def recebe(cerveja):
    cab=lista[0]
    dados=lista[1:]
    lista_cerveja=[]
    for dados_cerveja in dados:
    dict_cerveja={cab[0]:dados_cerveja[0],cab[1]:dados_cerveja[1],cab[2]:dados_cerveja[2],cab[3]:dados_cerveja[3],cab[4]:dados_cerveja[4],cab[5]:dados_cerveja[5],cab[6]:dados_cerveja[6]}
    lista_cerveja.apppend(dict_cerveja)
def consulta_preco(codigo):
    
   


lista = [
         ['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]
        ]
while