#em caso de variável booleana, não é necessária a validação(==True), pois o if já valida se o conteúdo da variável é True, senão vai para else
ativo=True
#só ocorre validação se a condição é verdadeira
if(ativo):
    print('Logar')
else:
    print('Não pode')
#caso a condição validada pelo if não seja verdadeira, o else é executado
ativo=False
if(ativo):
    print('Logar')
else:
    print('Não pode')
#variável booleana simples com True ou False
validador=False
validador=True
#criação da variável booleana através de expressão
#substituição do valor da variável
idade=18
validador=(idade!=18)
print(validador)
validador=(idade<18)
print(validador)
validador=(idade>18)
print(validador)
validador=(idade==18)
print(validador)
validador=(idade<=18)
print(validador)
validador=(idade>=18)
print(validador)
#inversão da expressão
validador=not True
validador=not False
validador=(idade>18 and idade<18)
validador=(idade<18 or idade==18)
#
lista_numeros=[3,4,6,2]
numero=2
if('Teti'.count('t')>0):
    print('Existe "t" em "teti')
if 'e' in 'Teti':
    print('Existe "t" em "teti"')
if 'm' in not 'Teti':
    print('Não exixste "m" em "Teti"')
if numero in lista_numeros:
    print('Existe')
else:
    print('Não existe')
lista_vazia=[]
if len(lista_numeros==0):
    print('Vazia')
else:
    print('Não vazia')  
lista_nomes=[]
if lista_nomes:
    print('Tem nomes')
else:
    print('Não tem nomes')
nome=''
print(nome)
nome='Marcela'
print(nome[2])
nome[2]='V'
print(nome)
if nome:
    print('Preenchido')
else:
    print('Vazio')
