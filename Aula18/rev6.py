# Festa da HBSIS
# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade
# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.
# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"
    # [{'código':'1','nome':'marcela beduschi','sexo':'f','idade':'18'},
    # {'código':'2','nome':'joana francisca','sexo':'f','idade':'16'},
    # {'código':'3','nome':'carlos alberto','sexo':'m','idade':'17'},
    # {'código':'4','nome':'joao vitor','sexo':'m','idade':'21'}]
class FestaHBSIS:
    #__init__ serve para iniciar as variáveis e disponibilizá-las para todos os métodos da classe
    #self é a ponta que irá conectar toda a classe e seus atributos 
    def __init__(self):
        self.lista=self.ler_cadastro()
    def ler_cadastro(self):
        arquivo=open('Aula18/cadastro.txt', 'r')
        self.lista=[]
        for pessoas in arquivo:
            pessoa=pessoa.strip().split(';')
            dicionario={'codigo':pessoa[0],'nome':pessoa[1],'sexo':pessoa[2],'idade':pessoa[3]}
            lista.append(dicionario)
        arquivo.close()
        return self.lista
    def lista_festa(self):
        lista_homens=[]
        lista_mulheres=[]
        for pessoa in lista_de_entrada:
            if int(pessoa['idade'])>=18:
                if (pessoa['sexo'])=='f':
                    lista_mulheres.append(pessoa)
                else:
                    lista_homens.append(pessoa)
            self.salvar(lista_mulheres,'mulheres')        
            self.salvar(lista_homens,'homens')
    def salvar(self,lista1,nome):
        arquivo=open(f'Aula18/{nome}.txt','a')
        for pessoa in lista1:
            texto=f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']}"
            arquivo.write(texto)
        arquivo.close()
    def consulta(self,num):
        for lista_consulta in self:
            if(lista_consulta['codigo']==num):
                if int(lista_consulta['idade']>=18):
                    if (lista_consulta['sexo']=='f'):
                        print(f"Nome:{lista_consulta['nome']}\nValor ingressso:R$15,00")
                    else:
                        print(f"Nome:{lista_consulta['nome']}\nValor ingresso:R$35,00")
                else:   
                    print('Não pode entrar')
    lista1=ler_cadastro()
    lista_festa(lista1)
    while True:
        a=int(input('Digite um número:'))
        consulta(lista1,a)
