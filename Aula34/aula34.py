#WEB
from flask import Flask
pessoa_controller=PessoaController()
app=Flask (__name__)
@app.route('/')
def inicio():
    return render_template('index.html',titulo_app='nome')
@app.route('/Listar')
def listar():
    return render_template('listar.html',titulo_app='nome',lista=pessoas)
@app.route('/Cadastrar')
def cadastrar():
    return render_template('cadastrar.html',titulo_app='nome')
app.run(debug=True)
