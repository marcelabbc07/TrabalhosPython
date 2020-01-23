from dao.squad_dao import SquadDao
from model.squad import Squad
from controller.squad_controller import SquadController

class FrameworkFrontEnd:
    dao=FrameworkFrontEndDao()
    squad_controller=SquadController()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self,id):
        return self.dao.buscar_por_id(id)

    def salvar(self,frameworkfrontend:FrameworkFrontEnd):
        frameworkfrontend.squad.id=self.squad_controller.salvar(squad.frameworkfrontend)
        return self.dao.salvar(frameworkfrontend)

    def alterar(self,frameworkfrontend:FrameworkFrontEnd):
        self.dao.alterar(frameworkfrontend)

    def deletar(self,id):
        self.dao.deletar(id)