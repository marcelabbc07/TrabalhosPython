# interação de lista com o for
# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.
# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.
# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.
cerveja = (('Marca:', 'Tipo:', 'IBU:','Preço:'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )
cab=cerveja[0]
dados=cerveja[1:]
for dados_cerveja in dados:
    print(f'{cab[0]}{dados_cerveja[0]}')
    print(f'{cab[1]}{dados_cerveja[1]}')
    print(f'{cab[2]}{dados_cerveja[2]}')
    print(f'{cab[3]}{dados_cerveja[3]}')