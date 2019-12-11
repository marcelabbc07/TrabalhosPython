# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.
# print(f'Codigo:{c.codigo}\nNome:{c.nome}\nIdade:{c.idade}\nSexo:{c.sexo}\nEmail:{c.email}\nTelefone:{c.telefone}')
class cliente:
    def __init__(self,dadobruto):
        self.dado_bruto=dadobruto
        self.codigo=None
        self.nome=None
        self.idade=None
        self.sexo=None 
        self.email=None
        self.telefone=None
    def adc_dados(self):
        pessoa=self.dado_bruto.strip().split(';')
        self.codigo=int(pessoa[0])
        self.nome=(pessoa[1])
        self.idade=int(pessoa[2])
        self.sexo=(pessoa[3])
        self.email=(pessoa[4])
        self.telefone=int(pessoa[5])
    def __str__(self):
        texto=f'''
Código:{self.codigo}
Nome:{self.nome}
Idade:{self.idade}
Sexo:{self.sexo}
Email:{self.email}
Telefone:{self.telefone}'''
        return texto
    def __eq__(self,valor):
        return self.codigo==valor
    def salvar_dados(self):
        arquivo=open('Aula23/dados.txt','a')
        arquivo.write(f"{salvar_dados['codigo']};{salvar_dados['nome']};{salvar_dados['idade']};{salvar_dados['sexo']};{salvar_dados['email']};{salvar_dados['telefone']}")
        arquivo.close()
    def att_dados():
        lista=[]
        arquivo=open('Aula23/dados.txt','+')
        for linha in lcliente:
            linha=linha.strip()
            lista_linha=linha.split(';')
            cliente={'codigo':lista_linha[0],'nome':lista_linha[1],'idade':lista_linha[2],'sexo':lista_linha[3],'email':lista_linha[4],'telefone':lista_linha[5]}
            lista.append(cliente)
        arquivo.close()
codigo=int(input('Digite o código do cliente:'))
nome=input('Digite o nome do cliente:')
idade=int(input('Digite a idade do cliente:'))
sexo=input('Digite o sexo do cliente:')
email=input('Digite o email do cliente:')
telefone=int(input('Digite o telefone do cliente:'))
lcliente=[]
c=cliente(dadobruto)
c.adc_dados()
lcliente.append(c)
dict_cliente={'codigo':codigo,'nome':nome,'idade':idade,'sexo':sexo,'email':email,'telfone':telefone}
salvar=salvar_dados(dict_cliente)
print(lcliente[0])