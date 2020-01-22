import MySQLdb
from model.squad import Squad

class SquadDao:
    conexao=MySQLdb.connect(host='localhost',database='aulabd',user='root',passwd='')
    cursor=conexao.cursor()

    def listar_todos(self):
        self.cursor.execute('SELECT * FROM squad')
        return self.cursor.fetchall()
    
    def buscar_por_id(self,id):
        self.cursor.execute(f"SELECT * FROM squad WHERE ID={id}")
        return self.cursor.fetchone()

    def salvar(self,squad:Squad):
        self.cursor.execute(f"INSERT into squad (NOME,DESCRICAO,NUMEROPESSOAS,LINGUAGEMBACKEND,FRAMEWORKFORNTEND) VALUES ('{self.nome}','{self.descricao}',{self.numeropessoas},'{self.linguagembackend}','{self.frameworkfrontend}')")
        self.conexao.commit()
        return self.cursor.lastrowid

    def alterar(self,squad:Squad):
        self.cursor.execute(f"UPDATE squad SET NOME='{squad.nome}',DESCRICAO='{squad.descricao}',NUMEROPESSOAS={squad.numeropessoas},LINGUAGEMBACKEND='{squad.linguagembackend}',FRAMEWORKFRONTEND='{squad.frameworkfrontend}' WHERE ID={id}")
        return self.conexao.commit()

    def deletar(self,id):
        self.cursor.execute(f'DELETE FROM squad WHERE ID={id}')
        return self.conexao.commit()