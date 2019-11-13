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