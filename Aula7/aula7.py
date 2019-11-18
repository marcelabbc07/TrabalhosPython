#dicionários
#criação de uma variável tipo dicionario
dicionario={'nome':'Marcela','sobrenome':'Beduschi'}
#impressão de um dicionário completo
print(dicionario)
#impressão de um dos dados do dicionário através de chave
print(dicionario['sobrenome'])
#criação de dicionário através de variáveis de tipos distintos
nome='Marcela'
lista_notas=[10,20,50,70]
#sum:soma todas as variáveis dentro de uma lista//len:divide pela quantidade das variáveis contidas na lista
media=sum(lista_notas)/len(lista_notas)
if(media>=7):
    situacao='Aprovado'
else:
    situacao='Reprovado'
dicionario_alunos={'nome':nome,'lista_notas':lista_notas,'media':media,'situacao':situacao}
#impressão de dados do dicionário através de suas chaves
print(f"{dicionario_alunos['nome']} - {dicionario_alunos['situacao']}")
#criação de um dicionário com valores padrão e alteração do valor posterior a criação
#é possível adicionar um novo valor a posição da chave
dicionario_bandas={}
dicionario_bandas['nome']='Sorority Noise'
#alteração do valor através de chave
dicionario_bandas['nome']='Thee Oh Sees'
print(dicionario_bandas)
#criação de um dicionário e adição de uma nova chave após a criação
#é possível adicionar novas informações no dicionário
dicionario={'nome':'Marcela','sobrenome':'Bianchini'}
dicionario['sobrenome']='Beduschi'
#adição de nova chave/valor ao dicionário existente
dicionario['cpf']='072.456.899-97'
print(dicionario)
#criação de um dicionário com dados de uma pessoa e através do laço de repetição adicionar em lista
lista_pessoa=[]
for i in range(0,10):
    dicionario_pessoa={'nome':'','sobrenome':'','cpf':'','rg':''}
    dicionario_pessoa['nome']=(input('Digite seu nome:'))
    dicionario_pessoa['sobrenome']=(input('Digite seu sobrenome:'))
    dicionario_pessoa['cpf']=(input('Digite seu cpf:'))
    dicionario_pessoa['rg']=(input('Digite seu rg:'))
    lista_pessoa.append(dicionario_pessoa)
    