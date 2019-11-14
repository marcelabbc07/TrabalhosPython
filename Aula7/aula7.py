#dicionários
dicionario={'nome':'Marcela','sobrenome':'Beduschi'}
print(dicionario)
print(dicionario['sobrenome'])
#sum:soma todas as variáveis dentro de uma lista//len:divide pela quantidade das variáveis contidas na lista
nome='Marcela'
lista_notas=[10,20,50,70]
media=sum(lista_notas)/len(lista_notas)
if(media>=7):
    situacao='Aprovado'
else:
    situacao='Reprovado'
dicionario_alunos={'nome':nome,'lista_notas':lista_notas,'media':media,'situacao':situacao}
print(f"{dicionario_alunos['nome']} - {dicionario_alunos['situacao']}")
#é possível adicionar um novo valor a posição da chave
dicionario_bandas={}
dicionario_bandas['nome']='Sorority Noise'
dicionario_bandas['nome']='Thee Oh Sees'
print(dicionario_bandas)
#é possível adicionar novas informações no dicionário
dicionario={'nome':'Marcela','sobrenome':'Bianchini'}
dicionario['sobrenome']='Beduschi'
dicionario['cpf']='072.456.899-97'
print(dicionario)
