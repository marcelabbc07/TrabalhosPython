import sys
sys.path.append('C:/Users/900146/Documents/git/TrabalhosPython/Aula33/exercicio1/aula33-4')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)