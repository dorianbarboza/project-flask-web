from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField


class Formulario(Form):
    username = StringField('Username')
    email = EmailField('Correo')
    comment = TextField('Comentario')
