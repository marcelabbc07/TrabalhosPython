from dao.squad_dao import SquadDao
from model.squad import Squad

class SquadController:
    dao=SquadDao()

    def listar_todos(self):
        return self.dao.listar_todos()
    
    def buscar_por_id(self,id):
        return self.dao.buscar_por_id(id)

    def salvar(self,squad:Squad):
        return self.dao.salvar(squad)

    def alterar(self,squad:Squad):
        return self.dao.alterar(squad)

    def deletar(self,id):
        return self.dao.deletar(id)

