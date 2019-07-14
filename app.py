from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

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

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
