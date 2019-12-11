# Aula 20 - 05-12-2019
# DICA: use o metodo round(valor,2) para arredondar os numeros para fazer
# a conta. Assim evita que o python use valores muito quebrados para as 
# contas.
# Exemplo:
# >>> round(2.7555,2)
# 2.76
# DICA2: Há 3 operadores matemáticos para a divisão: / // e o %
# / - é a divisão total entre os dois números. Pode resultar em numeros 
# reais.
# Exemplo: 5 / 3 = 1.6666666666666667
# // - é a divisão inteira. Ela vai resultar em números inteiros
# Exemplo: 5 // 3 = 1
# % - é o resto da divisão inteira. É o que sobra.
# Exemplo: 5 % 3 = 2
# 1 - Caixa eletrônico 
# Com estas listas de  dicionários:
# Monte um metodo que leia um valor e imprima (f-string) a quantidade de 
# cada nota(s) e moeda(s) necessária(s) para devolver o troco ao cliente.
# nota = [{'Nota(s)':100.00},{'Nota(s)':50.00},{'Nota(s)':20.00},
#         {'Nota(s)':10.00},{'Nota(s)':5.00},{'Nota(s)':2.00},]
            
            
# moeda = [{'Moeda(s)':1.00},{'Moeda(s)':0.50},{'Moeda(s)':0.25},
#          {'Moeda(s)':0.10},{'Moeda(s)':0.05},{'Moeda(s)':0.01}]

# def ler_valor(valor,n100,n50,n20,n10,n5,n2,m1,m50,m25,m10,m05,m01):
valor=float(input('Digite o valor:'))
round(valor,2)
n100=valor/100
n50=n100/50
n20=n50/20
n10=n20/10
n5=n10/5
n2=n5/2

print(f'Notas de 100:{n100}\nNotas de 50:{n50}\nNotas de 20:{n20}\nNotas de 10:{n10}\nNotas de 5:{n5}\nNotas de 2:{n2}')
# print(f'Moedas de 1:{m1}\nMoedas de 0.50:{m50}\nMoedas de 0.25:{m25}\nMoedas de 0.10:{m10}\nMoedas de 0.05:{m05}\nMoedas de 0.01:{m01}')



