from dao.squad_dao import SquadDao
from model.squad import Squad
from controller.squad_controller import SquadController

class SGBDController:
    dao=SGBDDao()
    squad_controller=SquadController()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self,id):
        return self.dao.buscar_por_id(id)

    def salvar(self,sgbd:SGBD)
        sgbd.squad.id=self.squad_controller.salvar(squad.sgbd)      
        return self.dao.salvar(sgbd)

    def alterar(self,sgbd:SGBD)
        self.dao.alterar(sgbd)

    def deletar(self,id):
        self.dao.deletar(id)