from dao.squad_dao import SquadDao
from model.squad import Squad
from controller.squad_controller import SquadController

class LinguagemBackEndController:
    dao=LinguagemBackEndDao()
    squad_controller=SquadController()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self,id):
        return self.dao.buscar_por_id(id)

    def salvar(self,linguagembackend:LinguagemBackEnd)
        linguagembackend.squad.id=self.squad_controller.salvar(squad.linguagembackend)      
        return self.dao.salvar(linguagembackend)

    def alterar(self,linguagembackend:LinguagemBackEnd)
        self.dao.alterar(linguagembackend)

    def deletar(self,id):
        self.dao.deletar(id)