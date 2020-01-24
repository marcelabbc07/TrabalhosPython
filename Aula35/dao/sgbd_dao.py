import MySQLdb
from model.sgbd import SGBD

class SGBDDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        self.cursor.execute(f"SELECT * FROM sgbd AS B LEFT JOIN squad AS S ON S.SGBD_ID=B.ID")
        return self.cursor.fetchall()    
    
    def buscar_por_id(self,id):
        self.cursor.execute(f"SELECT * FROM sgbd AS B LEFT JOIN squad AS S ON S.SGBD_ID=S.ID WHERE B.ID={id}")
        return self.cursor.fetchone()        

    def salvar(self,sgbd:SGBD):
        self.cursor.execute(f"INSERT INTO sgbd (SGBD) VALUES ('{sgbd.sgbd}')")
        self.conexao.commit()
        return self.cursor.lastrowid

    def alterar(self,sgbd:SGBD):
        self.cursor.execute(f" UPDATE sgbd SET sgbd='{sgbd.sgbd}' WHERE ID={sgbd.id}")
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self,id):
        self.cursor.execute(f'DELETE FROM sgbd WHERE ID={id}')
        self.conexao.commit()