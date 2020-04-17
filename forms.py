from wtforms import Form
from wtforms import StringField, TextField
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import HiddenField
from models import User


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class CommentForm(Form): #utiliza el formato para facilidar la lectura HTML en comentarios
    comment = TextField('Comentario')
    honeypot = HiddenField('', [length_honeypot])

class LoginForm(Form): #utiliza el formato para facilidar la lectura HTML en el login del usuario y ayuda a su validacion respectiva
    username = StringField('Nombre Usario',
        [
        validators.Required(message='El Nombre del Usuario es Requerido!.'),
        validators.length(min=6, max=12, message='Ingrese un usuario Valido!.') 
        ])
    password = PasswordField('Password',
        [
        validators.Required(message='El Password Requerido!.'),
        ]
    )

class CreateForm(Form): #utiliza el formato para facilidar la lectura HTML en creacion de usuario
    username = StringField('Login de Usuario',
        [
        validators.Required(message='El Nombre del Usuario es Requerido!.'),
        validators.length(min=6, max=12, message='Ingrese un usuario Valido!.')
        ]    
    )
    nombre = StringField('Nombre del Usuario',
        [
        validators.Required(message='El nombre del Usuario es Requerido!.'),
        validators.length(min=2, max=16, message='Ingrese un nombre Valido!.')
        ]    
    )
    apellido = StringField('Apellido de Usuario',
        [
        validators.Required(message='El apellido del Usuario es Requerido!.'),
        validators.length(min=2, max=16, message='Ingrese un usuario Valido!.')
        ]    
    )
    email = EmailField('Correo Electronico',
        [
        validators.Required(message='El Correo Electronico es Requerido!.'),
        validators.Email(message='Ingrese un Correo Electronico Valido!.')
        ]
    )
    password = PasswordField('Password',
        [
        validators.Required(message='El Password Requerido!.'),
        ]
    )

    def validate_username(form, field):# valida que el usuario que se desea crear no exista
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('Login del Usuario ya Existe')

class PassForm(Form): #este es el form que ayuda a cambiar el password actual por uno nuevo
    password = PasswordField('Password',
        [
        validators.Required(message='El Password Requerido!.'),
        ]
    )