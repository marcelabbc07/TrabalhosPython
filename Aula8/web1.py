#web
from flask import Flask
app=Flask(__name__)
@app.route('/')
def inicio():
    return 'Bem vindos'
app.run()