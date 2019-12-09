#atributos --- variáveis
nome 
idade 
sexo 
telefone

#metodos (função/procedimento)
respira
dorme
come
bebe
multiplica

#atributos de estado --- variáveis
divida
cansada
viva
fome
sede

class pessoa:
    def __init__(self,nome1,idade1,sexo1,telefone1):
        self.nome=nome1
        self.idade=idade1
        self.sexo=sexo1
        self.telefone=telefone1
        self.divida=None 
        self.cansada='não'
        self.viva=True
        self.fome='não'
        self.sede='não'
    def respira(self):
        if self.viva==True:
            if respirar==True:
                self.viva=True
            else:
                self.viva = False
    def corre(self,distancia):
        if self.viva:
            if self.distancia>=50 and distancia<100:
                self.cansada='pouco'
                self.sede='pouco'
                self.fome='pouco'
            elif self.distancia>=100 and distancia<200:
                self.cansada='medio'
                self.sede='medio'
                self.fome='medio'
            elif self.distancia>=200:
                self.cansada='muito'
                self.sede='muito'
                self.fome='muito'
    def dorme(self):
        if self.viva:
            self.cansada='não'
    def come(self):
        if self.viva:
            self.fome='não'
    def bebe(self):
        if self.viva:
            self.sed='não'
    def multiplica(self):
        pass
p=Pessoa()

