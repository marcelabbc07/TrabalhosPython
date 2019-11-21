nome_pagina='Calculadora'
from flask import Flask, render_template, request
from calculos import soma,sub,mult,div_int,div_fra,resto,raiz
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('aula10.html',titulo=nome_pagina) 
@app.route('/calcular')
def calcular():
    n1=int(request.args['n1'])
    n2=int(request.args['n2'])
    r_soma=soma(n1,n2)
    r_sub=sub(n1,n2)
    r_mult=mult(n1,n2)
    r_div_int=div_int(n1,n2)
    r_div_fra=div_fra(n1,n2)
    r_resto=resto(n1,n2)
    r_raiz=raiz(n1,n2)
    resultados={'soma':r_soma,'sub':r_sub,'mult':r_mult,'div_int':r_div_int,'div_fra':r_div_fra,'resto':r_resto,'raiz':r_raiz}
    return render_template('resultado.html',n1=n1,n2=n2,f"{resultados['soma']},{resultados['sub']},{resultados['mult']},{resultados['div_int']},{resultados['div_fra']},{resultados['resto']},{resultados['raiz']}")
app.run()