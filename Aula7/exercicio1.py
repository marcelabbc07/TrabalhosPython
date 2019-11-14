c_marca=str(input('Digite a marca da cerveja:'))
c_tipo=str(input('Digite o tipo da cerveja:'))
c_ibu=(input('Digite o IBU da cerveja:'))
c_abv=(input('Digite o ABV da cerveja:'))
c_ebc=(input('Digite o EBC da cerveja:'))
c_volume=(input('Digite o volume da cerveja:'))
dicionario_cerveja={'marca':c_marca,'tipo':c_tipo,'ibu':c_ibu,'abv':c_abv,'ebc':c_ebc,'volume':c_volume}
print(f"Marca:{dicionario_cerveja['marca']}\nTipo:{dicionario_cerveja['tipo']}\nIBU:{dicionario_cerveja['ibu']}\nABV:{dicionario_cerveja['abv']}\nEBC:{dicionario_cerveja['ebc']}\nVolume:{dicionario_cerveja['volume']}\n")
