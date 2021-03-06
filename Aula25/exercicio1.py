# Cliente.....

# Crie uma classe cliente.
# Use os seguintes atributos: codigo cliente(int), nome, idade(int), telefone, email, endereço
# Use o seguinte atributo de estado: crédito em R$, saldo R$, 
#                                    cliente_devedor(True/False)
# O atributo cliente_devedor deve ser True toda vez que o saldo negativo for menor 
# ou igual ao crédito. 
# Para o atributo cliente_devedor voltar a ser False o cliente deve pagar sua divida
# ficando com o saldo igual a 0 ou positivo.



# Como metodo use:
class Cliente:
    def __init__(self,codigo, nome, idade, telefone, email, endereco):
        self.codigo=None
        self.nome=None 
        self.idade=None 
        self.telefone=None 
        self.email=None 
        self.endereco=None
    def atualizar (self):
        dados=self.dado_bruto
        dados=dados.strip()
        dados=dados.split(';')
        self.codigo=int(dados[0])
        self.nome=(dados[1])
        self.idade=int(pessoa[2])
        self.email=(dados[3])
        self.telefone=(dados[4])
        self.endereco=int(dados[5])

    def limite_credito(self,valor):
        '''
        O crédito é o valor máximo que o cliente pode ter de saldo negativo.
        Este metodo altera o valor tanto para aumentar o crédito quanto para 
        diminuir ou eliminar o crédito.
        Este valor deve ser passado como número negativo (ex: -50.00) para o atributo
        credito
        Se diminuir o crédito (exemplo de -50 para -10) e o 
        cliente ficar com o saldo menor que o cédito (exemplo saldo = -20 e cédito -10)
        o cliente_devedor fica True
        Se o cliente_devedor estiver True, o crédito pode ser diminuido porem não aumentado.
        
        '''
        pass

    def dinheiro(self,valor):
        '''
        Este metodo serve para adicionar/remover valor em R$ para o atributo saldo para 
        o cliente.
        Esta função revebe o valor como parametro. Se o valor for positivo, o saldo
        aumenta, se o valor for negativo o saldo diminui. 
        
        O cliente não pode ter seu saldo menor que o crédito. Então se o valor exceder
        deve retornar False e a operação fica cancelada.
        (Exemplo: limite do cartão de crédito)
        Caso o valor não exceda o crédito a operação será realizada, o valor do saldo
        irá diminuir e deve retornar True
        Se o cliente_devedor estiver True o dinheiro só poderá receber valores positivos.
        Se o cliente_devedor estiver True e o cliente depositar dinheiro suficiente para
        o saldo ficar maior ou igual a 0 o cliente_devedor deve ser alterado para False.
        '''
        pass

    def __eq__(self,valor):
         return self.codigo==valor
    def __srt__(self):
      texto=f'''
Código:{self.codigo}
Nome:{self.nome}
Idade:{self.idade}
Telefone:{self.telefone}
Email:{self.email}
Endereço:{self.endereco}'''
    return texto
if __name__ == "__main__":

    '''
    Use este if para fazer os testes com a classe.
    Este if pergunta se este arquivo está sendo executado diretamente.
    Caso positivo o código será executado.
    '''
    pass
pessoa=cliente(dadobruto)
print(f'Código:{pessoa.codigo}\nNome:{pessoa.nome}\nIdade:{pessoa.idade}\nTelefone:{pessoa.telefone}\nEmail:{pessoa.email}\nEndereço:{pessoa.endereco}')
