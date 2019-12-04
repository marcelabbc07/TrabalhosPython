# Ao receber a seguinte lista, faça um metodo que retorne cada um destes itens de forma individual 
# com cabaçalho dizendo em que posição estes itens estão dentro da lista principal:
# Exemplo: 
# ############# posição 0 ##################
# Agua
# mamão
# ############# posição 1 ##################
# banana
# limão
#Regra: Não pode usar a função range e no máximo 2 print()
lista = [
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
          ['skol','kaiser','sol','schin','brahma','itaipava','bavaria'],
          ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha'],
          ['rizoto','macarronada','polenta','guizado','dobradinha','revirado','pure'],
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
          ['agua','cachoeira','rio','lagoa','sanga','brejo','laguna'],
          ['vento','ciclone','tufão','furacão','brisa','minuano','zefiro'],
          ['carro','moto','vespa','caminhão','sprinter','kombi','fusca'],
          ['calça','camisa','japona','jaqueta','camiseta','bone','regata']
        ]
def lista_item(lista):
  a=0
  for lista_a in lista:
    print(f'### POSIÇÃO {a} ### ')
    a=a+1
    for itens in lista_a:
      print(itens)
lista=lista_item(lista)
# while True:
#     b+=1
#     a+=1
#     print(f'### POSIÇÃO {a} ###\n{lista[0][0+b]}\n{lista[1][0+b]}\n{lista[2][0+b]}\n{lista[3][0+b]}\n{lista[4][0+b]}\n{lista[5][0+b]}\n{lista[6][0+b]}\n{lista[7][0+b]}\n{lista[8][0+b]}')
  