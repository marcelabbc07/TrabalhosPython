import MySQLdb
from model.linguagembe import LinguagemBackEnd

class LinguagemBackEndDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        self.cursor.execute(f"SELECT * FROM linguagembackend AS L LEFT JOIN squad AS S ON S.LINGUAGEMBACKEND_ID=L.ID")
        return self.cursor.fetchall()    
    
    def buscar_por_id(self,id):
        self.cursor.execute(f"SELECT * FROM linguagembackend AS L LEFT JOIN squad AS S ON S.LINGUAGEMBACKEND_ID=S.ID WHERE L.ID={id}")
        return self.cursor.fetchone()        

    def salvar(self,linguagembackend:LinguagemBackEnd):
        self.cursor.execute(f"INSERT INTO linguagembackend (LINGUAGEMBACKEND) VALUES ('{linguagembackend.linguagembackend}')")
        self.conexao.commit()
        return self.cursor.lastrowid

    def alterar(self,linguagembackend:LinguagemBackEnd):
        self.cursor.execute(f" UPDATE linguagembackend SET LINGUAGEMBACKEND='{linguagembackend.linguagembackend}' WHERE ID={linguagembackend.id}")
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self,id):
        self.cursor.execute(f'DELETE FROM linguagembackend WHERE ID={id}')
        self.conexao.commit()