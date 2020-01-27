import sys
sys.path.append('C:/Users/900146/Documents/git/TrabalhosPython/Aula35')
from controller.squad_controller import SquadController
from model.squad import Squad

squad=Squad()
squad.nome='Maykon'
squad.descricao='Professor'
squad.numeropessoas=1
squad.linguagembackend='Python'
squad.frameworkfrontend='Bootstrap'
squad.sgbd='MySQL Workbench'

contr=SquadController()
id_salvo=contr.salvar(squad)
print(contr.buscar_por_id(id_salvo))
