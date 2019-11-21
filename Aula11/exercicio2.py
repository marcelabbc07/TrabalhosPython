def rent(valor,juros,ano):
    rent=valor*((1+(juros/100))**ano)
    return rent
def juros_composto(rent,valor):
    juros_composto=rent-valor
    return juros_composto
valor=float(input('Digite o valor investido:'))
juros=float(input('Digite a taxa de juros:'))
ano=int(input('Digite a quantidade de anos:'))
rent=rent(valor,juros,ano)
juros_composto=juros_composto(rent,valor)
print(f'A rentabilidade anual do investimento é de:R${rent:.2f} e {juros_composto:.2f}%')