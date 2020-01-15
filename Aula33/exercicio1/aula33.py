# from pessoa_db import listar_todos
# from pessoa_convert import converter_tabela_dict
# from pessoa_export import exportar_txt
from pessoa import Pessoa
p1=Pessoa()
print(p1.id)
# lpt=listar_todos()
# lpd=converter_tabela_dict(lpt)
# exportar_txt(lpd)
def __str__(self):
    return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco_id}'
    