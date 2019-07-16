# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template

import forms

app = Flask(__name__, template_folder = 'templates_html')

@app.route('/')
def home():
    return 'home page'

""" RUTAS Y PARAMETROS """

@app.route('/params1')
def params1():
    # Parametros
    # http://127.0.0.1:8000/params1?name1=Dorian
    # http://127.0.0.1:8000/params1?name=Dorian&lastname=Barboza
    name = request.args.get('name', 'No hay parametro')
    lastname = request.args.get('lastname', 'No hay parametro')
    return 'El parametro es: {} {}'.format(name, lastname)

@app.route('/params2/')
@app.route('/params2/<name>/')
@app.route('/params2/<lastname>/')
@app.route('/params2/<name>/<lastname>/')
def params2(name = 'Nulo', lastname = 'Nulo'):
    # http://127.0.0.1:8000/params2/Dorian/Barboza/
    return 'El parametro es: {} {}'.format(name, lastname)

""" VALIDAR RUTA CON INT """
@app.route('/params3/<table>/<int:id>/')
def params3(table = 'Nulo', id = 'Nulo'):
    # http://127.0.0.1:8000/params3/usuario/1/
    return 'El parametro es: {} {}'.format(table, id)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/pruebas/<name>/')
def pruebas(name = 'Nulo'):
    # Lista = [] Corchetes
    # Tupla = () Parentecis
    # Diccionairio = JSON
    lastname = 'Barboza'
    name_complete = ["Dorian", "Barboza"]
    age = 18
    return render_template('pruebas.html', name_html = name, lastname_html = lastname, name_complete_html = name_complete, age_html = age)

""" Herencia de plantillas """
@app.route('/herencia/')
def herencia():
    nombre = "Dorian"
    return render_template('herencia.html', nombre_html = nombre)

@app.route('/usuarios/')
def usuarios():
    list_users = ['Dorian', 'Andy', 'Eyden']
    return render_template('usuarios.html', list_users_html = list_users)

""" Archivos estaticos """
@app.route('/staticFiles/')
def staticFiles():
    return render_template('static.html')

""" Templates herencia """
@app.route('/login_cliente/<name>/<lastname>/')
def login_cliente(name = 'Nulo', lastname = 'Nulo' ):
    return render_template('login_cliente.html', name_html = name, lastname_html = lastname)

""" Templates herencia y Macros """
@app.route('/login_usuario/<name>/<lastname>/')
def login_usuario(name = 'Nulo', lastname = 'Nulo'):
    return render_template('login_usuario.html', name_html = name, lastname_html = lastname)

@app.route('/formulario/', methods = ['GET', 'POST'])
def formulario():
    formulario = forms.Formulario(request.form)

    if request.method == 'POST':
        print(formulario.username.data)
        print(formulario.email.data)
        print(formulario.comment.data)

    return render_template('formulario.html', form = formulario)

""" App """
@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
