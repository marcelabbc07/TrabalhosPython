# Aula 19 - 04-12-2019
# Lista com for e metodos
# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 
# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com
# 2 - usando o for, imprima todos nomes um abaixo do outro
#
# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados 
# do Mateus, Paulo # e João contendo
# como chaves: nome, email, idade, telefone (nesta  sequencia)
cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]
print(f'{cadastroHBSIS[0]}:{cadastroHBSIS[1][0]} - {cadastroHBSIS[2]}:{cadastroHBSIS[3][0]}')
print(f'A idade de {cadastroHBSIS[1][4]} é {cadastroHBSIS[7][4]} anos')
print(f'O email de {cadastroHBSIS[1][3]} é {cadastroHBSIS[5][3]}')
a=-1
for i in range(7):
    a=a+1
    print(f'{cadastroHBSIS[0]}:{cadastroHBSIS[1][a]}')
lista=[]
cab=cadastroHBSIS[0::2]  #pula de 2 em 2 diretamente na lista
dados=cadastroHBSIS[1::2]
for lista in dados:
    print(lista)
    for item in lista:
        print(item)
# lista_cads=[]
# cad_m={'nome':cadastroHBSIS[1][3],'email':cadastroHBSIS[5][3],'idade':cadastroHBSIS[6][3],'telefone':cadastroHBSIS[3][3]}
# cad_p={'nome':cadastroHBSIS[1][1],'email':cadastroHBSIS[5][1],'idade':cadastroHBSIS[6][1],'telefone':cadastroHBSIS[3][1]}
# cad_j={'nome':cadastroHBSIS[1][5],'email':cadastroHBSIS[5][5],'idade':cadastroHBSIS[6][5],'telefone':cadastroHBSIS[3][5]}
# lista_cads.append(cad_m)
# lista_cads.append(cad_p)
# lista_cads.append(cad_j)
# print(lista_cads)