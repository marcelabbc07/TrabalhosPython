import sys
sys.path.append('')
from model.endereco import Endereco
from dao.endereco_dao import EnderecoDao

class EnderecoController:
    dao=EnderecoDao()

    def listar_todos(self):
        return self.dao.listar_todos

    def buscar_id(self,id):
        return self.dao.buscar_id(id)
    
    def salvar(self,endereco:Endereco):
        self.dao.salvar(endereco)

    def alterar(self,endereco:Endereco):
        self.dao.alterar(endereco)
    
    def deletar(self,id):
        self.dao.deletar(id)

    controller=EnderecoController()
    e=controller.buscar_id(1)
    e=controller.listar_todos()
    print(e)