def selic(cota):
    selic=(5/100)+(2/100)
    return selic
cota=float(input('Digite quantas cotas tu desejas investir:'))
selic=selic(cota)
if(cota>=0.01):
    for i in range(1,65,1):
        cota=(10410*cota)
        print(f'{i}-O valor total até o vencimento do título é de:R${cota:.2f}')
else:
    print('Digite uma cota válida')

