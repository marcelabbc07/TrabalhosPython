import MySQLdb
conexao=MySQLdb.connect(host='localhost',database='aulabd',user='root',passwd='')
cursor=conexao.cursor()
def listar_todos(c):
    c.execute('SELECT * FROM endereco')
    enderecos=c.fetchall()
    for e in endereco:
        print(e)
def buscar_id(c):
    c.execute(f'SELECT * FROM endereco WHERE ID={id}')
    endereco=c.fecthone()
    print(endereco)
def buscar_logradouro(c,logradouro):
    c.execute(f"SELECT * FROM endereco WHERE LOGRADOURO like '{logradouro}%'")
    for e in c.fetchall():
        print(e)
def salvar(cn,cr,id,logradouro,numero,complemento,bairro,cidade):
    cr.execute(f"INSERT INTO endereco (LOGRADOURO,NUMERO,COMPLEMENTO,BAIRRO,CIDADE) VALUES ('{logradouro}',{numero},'{complemento}','{bairro}','{cidade}')")
    cn.commit()
def alterar(cn,cr,id,logradouro,numero,complemento,bairro,cidade):
    cr.execute(f"UPDATE endereco SET LOGRADOURO='{logradouro}',{numero},'{complemento}','{bairro}','{cidade}' WHERE ID={id}")
    cn.commit()
def deletar(cn,cr,id):
    cr.execute(f'DELETE FROM endereco WHERE ID={id}')
    cn.commit()
# buscar_id(cursor,1)
# buscar_logradouro(cursor,'Au')
# salvar(conexao,cursor,2,'Rua Francisco Alcântara',96,'Sem complemento','Ponta Aguda','Blumenau')
alterar(conexao,cursor,2,'Rua Francisco Alcântara',96,'Próximo ao anel viário','Ponta Aguda','Blumenau')
# deletar(conexao,cursor,2)
