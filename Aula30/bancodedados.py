#Banco de Dados
#SGBD - Sistema Gerenciador de Banco de Dados
#MySQL - MariaDb
#SELECT *(ALL) FROM PESSOA(TABELA INTEIRA) WHERE(FILTRA UM LOCAL ESPECÍFICO) ID = 1
#INSERT INTO PESSOA 
#(
#    NOME
#    ,SOBRENOME
#    ,IDADE    
#)
#VALUES
#(
#    'TAVINHO'
#    ,'HONDA'
#    ,15
#)
#CRUD 
#C=CREATE
#R=READ
#U=UPDATE 
#D=DELETE
# 
#UPDATE PESSOA 
#SET IDADE = 24
#WHERE ID = 1 OR ID = 4
# 
#INSERT INTO PESSOA
#(
#    NOME
#    ,SOBRENOME
#)
#VALUES
#(
#   'TONHAO'
#   ,'CARREGADO'# 
#) 
# 
#DELETE FROM PESSOA WHERE ID = 4
# 
# 
# 
from flask_mysqldb import MySQLdb
from contextlib import closing
__dados={'host':"mysql.topskills.study",'database':"topskills01",'user':"topskills01",'password':"ts2019",'port':3306}
def cadastrar(nome,idade):
    with closing(MySQLdb.connect(**__dados)) as conn:
        cursor=conn.cursor()
        cursor.execute(f"INSERT INTO topskills.Marcela (nome,idade) VALUES ('{nome})',{idade};")
        conn.commit()
def consultarAll():
    with closing(MySQLdb.connect(**__dados)) as conn:
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM Marcela')
        print('\nSó uma linha:',cursor.fetchone())
        print('\nVárias linhas:',cursor.fetchall())
for i in range(3):
    nome=input('Digite seu nome:')
    idade=int(input('Digite sua idade:'))
    cadastrar(nome,idade)
consultarAll()