import MySQLdb
from model.endereco import Endereco

class EnderecoDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()
    
    def listar_todos(self):
        comando_sql_select = "SELECT * FROM endereco"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()
        lista_enderecos_classe = self.converter_tabela_classe(resultado)
        return lista_enderecos_classe

    def buscar_por_id(self, id):
        comando_sql_select = f"SELECT * FROM endereco WHERE ID= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        lista_pessoas = []
        for e in lista_tuplas:
            e1 = Endereco()
            e1.id = e[0]
            e1.logradouro = e[1]
            e1.numero= e[2]
            e1.complemento = e[3]
            e1.bairro = e[4]
            e1.cidade = e[5]
            lista_enderecos.append(p1)
        return lista_enderecos
    def salvar(self,endereco):
        comando=f"INSERT INTO endereco (LOGRADOURO,NUMERO,COMPLEMENTO,BAIRRO,CIDADE) VALUES ('{endereco.logradouro}','{endereco.numero}','{endereco.complemento}','{endereco.bairro}','{endereco.cidade}')"
        self.cursor.execute(comando)
        self.conexao.commit()   
    def alterar(self,pessoa):
        comando=f"UPDATE endereco SET LOGRADOURO='{endereco.logradouro}',NUMERO={endereco.numero},COMPLEMENTO='{endereco.complemento}',BAIRRO='{endereco.bairro}',CIDADE='{endereco.cidade}'"
        self.cursor.execute(comando)
        self.conexao.commit()
    def deletar(self,endereco):
        comando=f'DELETE FROM endereco WHERE ID={id}'
        self.cursor.execute(comando)
        self.conexao.commit()