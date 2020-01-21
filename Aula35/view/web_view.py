from flask import Flask,render_template,request,redirect
import sys
sys.path.append('C:/Users/900146/Documents/git/TrabalhosPython/Aula35')
from controller.squad_controller import SquadController
from model.squad import Squad

app=Flask(__name__)
squad_controller=SquadController()
nome='Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html',titulo_app=nome)

@app.route('/listar')
def listar():
    squad=squad_controller.listar_todos()
    return render_template('listar.html',titulo_app=nome)

@app.route('/cadastrar')
def cadastrar():
    pass

@app.route('/excluir')
def excluir():
    pass

@app.route('/slavar')
def salvar():
    pass