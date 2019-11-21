def iss(valor):
    iss=valor*(2/100)
    return iss
valor=float(input('Digite o valor do serviço:'))
iss=iss(valor)
print(f'O valor do imposto ISS é de:R${iss}')