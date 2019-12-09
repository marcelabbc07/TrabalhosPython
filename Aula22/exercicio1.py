class cliente:
    def __init__(self,codigo,cpf,nome,idade,sexo):
        self.cod=codigo
        self.cpf=cpf
        self.nome=nome
        self.idade=idade
        self.sexo=sexo
        self.salario=True
        self.carteira='sim'
        self.bens='sim'
        self.dividas='não'
    def recebe_sal(self):
        if self.salario==True:    
            if self.carteira==True:
                self.salario=True
            else:
                self.salario=False
    def comprar(self):
        if self.carteira>=self.bens:
            self.bens='sim'
        elif self.carteira<self.bens:
            self.bens='sim'
            self.dividas='sim'
        else:
            self.bens='não'
    def pagar_divida(self):
        if self.carteira>=self.dividas:
            self.dividas='não'
        else:
            self.dividas='sim'
c=cliente('1','000','Marcela','19','F')
print(f'Tem dinheiro na carteira? {c.carteira}')
print(f'Tem bens? {c.bens}')
print(f'Tem dívidas? {c.dividas}') 