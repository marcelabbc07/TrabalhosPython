import MySQLdb
conexao=MySQLdb.connect(host='localhost',database='aulabd',user='root',passwd='')
cursor=conexao.cursor()
def listar_todos(c):
    c.execute('SELECT * FROM pessoa')
    pessoas=cursor.fetchall()
    for p in pessoas:
        print(p)
def buscar_id(c,id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa=c.fetchone()
    print(pessoa)
def buscar_sn(c,sobrenome):
    c.execute(f"SELECT * FROM pessoa WHERE SOBRENOME like '{sobrenome}%'")
    for p in cursor.fetchall():
        print(p)
def salvar(cn,cr,nome,sobrenome,idade,endereco_id='Null'):
    cr.execute(f"INSERT INTO pessoa (NOME,SOBRENOME,IDADE,ENDERECO_ID VALUES ('{nome}','{sobrenome}',{idade},{endereco_id}))")
    cn.commit()
def alterar(cn,cr,id,nome,sobrenome,idade,endereco_id='Null'):
    cr.execute(f"UPDATE pessoa SET NOME='{nome}','{sobrenome}',{idade},{endereco_id} WHERE ID={id}")
    cn.commit()
def deletar(cn,cr,id):
    cr.execute(f'DELETE FROM pessoa WHERE ID={id}')
    cn.commit()
# buscar_id(cursor,1)
# buscar_sn(cursor,'Be')
# salvar(conexao,cursor,'Josué','KingOfList',30)
# alterar(conexao,cursor,2,'Voltolini','KingOfBasquete',16)
deletar(conexao,cursor,3)