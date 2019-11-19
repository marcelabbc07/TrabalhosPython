#web
from flask import Flask
app=Flask(__name__)
@app.route('/')
def inicio():
    return 'Bem vindos'
app.run()
app.run(host='192.168.0.120',port=80)