import sys
sys.path.append('')
from model.pessoa import Pessoa
from dao.pessoa_dao import PessoaDao

class PessoaController:
    dao=PessoaDao()

    def listar_todos(self):
        return self.dao.listar_todos

    def buscar_id(self,id):
        return self.dao.buscar_id(id)
    
    def salvar(self,pessoa:Pessoa):
        self.dao.salvar(pessoa)

    def alterar(self,pessoa:Pessoa):
        self.dao.alterar(pessoa)
    
    def deletar(self,id):
        self.dao.deletar(id)

    controller=PessoaController()
    p=controller.buscar_id(1)
    p=controller.listar_todos()
    print(p)