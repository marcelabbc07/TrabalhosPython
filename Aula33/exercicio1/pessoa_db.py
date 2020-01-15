#Importar biblioteca do Mysql
import MySQLdb
#Classes
class PessoaDb:
#Configurar a conexão
    conexao=MySQLdb.connect(host='localhost',database='aulabd',user='root',passwd='')
#Salva o cursor da conexão
    cursor=conexao.cursor()
def listar_todos(self):
#Criação do dicionário que representa uma pessoa
#Criação do comando SQL é passado para o cursor
    self.cursor.execute('SELECT * FROM pessoa')
    pessoas=self.cursor.fetchall()
    return pessoas
def buscar_id(self,id):
    self.cursor.execute('SELECT * FROM pessoa WHERE ID={id}')
    self.cursor.fetchone()
    return resultado