#Flask RestFul
#Get
#Post
#Put
#Delete
from flask import Flask
from flask_restful import Api,Resource
from Controller.cerveja_controller import CervejaController

app=Flask(__name__)
api=Api(app)
api.add_resource(CervejaController,'/api/cerveja')

@app.route('/')
def inicio():
    return 'Bem vindo a API'

app.run(debug=True,port=80)