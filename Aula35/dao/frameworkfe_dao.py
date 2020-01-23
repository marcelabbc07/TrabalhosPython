import MySQLdb
from model.frameworkfe import FrameworkFrontEnd

class FrameworkFrontEndDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        self.cursor.execute(f"SELECT * FROM frameworkfrontend AS F LEFT JOIN squad AS S ON S.FRAMEWORKFRONTEND_ID=F.ID")
        return self.cursor.fetchall()    
    
    def buscar_por_id(self,id):
        self.cursor.execute(f"SELECT * FROM frameworkfrontend AS F LEFT JOIN squad AS S ON S.FRAMEWORKFRONTEND_ID=S.ID WHERE F.ID={id}")
        return self.cursor.fetchone()        

    def salvar(self,frameworkfrontend:FrameworkFrontEnd):
        self.cursor.execute(f"INSERT INTO frameworkfrontend (FRAMEWORKFRONTEND) VALUES ('{frameworkfrontend.frameworkfrontend}')")
        self.conexao.commit()
        return self.cursor.lastrowid

    def alterar(self,frameworkfrontend:FrameworkFrontEnd):
        self.cursor.execute(f" UPDATE frameworkfrontend SET FRAMEWORKFRONTEND='{frameworkfrontend.frameworkfrontend}' WHERE ID={frameworkfrontend.id}")
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self,id):
        self.cursor.execute(f'DELETE FROM frameworkfrontend WHERE ID={id}')
        self.conexao.commit()