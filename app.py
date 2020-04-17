from flask import Flask, jsonify, request, flash, url_for, redirect
from flask import session
from flask import render_template
from flask_wtf import CsrfProtect
from flask import make_response
from flask import g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from config import DevelopmentConfig
from models import db
from models import User
from models import Comment
from models import Teams

import json
import forms


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect()

#administrador de error en caso de que la pagina no exista.
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.after_request
def after_request(response):
	return response

#Session del super usuario desde aqui se administra la aplicacion.
@app.route('/index1', methods = ['GET','POST'])
def index():
	if 'username' in session: 
		username = session['username']
		title = 'Examen 02'
	return render_template('index1.html', title = title)

#applicacion que permite a un usuario valido y existente pueda ingresar a generar a la aplicacion
@app.route('/', methods = ['GET','POST'])
def login():
	login_form = forms.LoginForm(request.form)
	if request.method == 'POST' and login_form.validate():
		username = login_form.username.data
		password = login_form.password.data
		user = User.query.filter_by(username = username).first()
		session['user_id'] = user.id
		print(username)
		if username == 'superuser': #si es super usuario lo envia al menu administrativo, si es usuario normar, puede generar comentarios
			return redirect( url_for('index') )
		else:
			if user is not None and user.verify_password(password):
				success_message = 'Bienvenido {}'.format(username)
				flash(success_message)
				session['username'] = username
				return redirect( url_for('comment') )
			else:
				error_message = 'Usuario o passsord no Validos!'
				flash(error_message)
	return render_template('login.html', form = login_form)

#applicacion que cierra la session del usuario activo
@app.route('/logout')
def logout():
	if 'Username' in session:
		session.pop('Username')
	return redirect(url_for('login'))

#applicacion que permite crear usuarios, si el usuario existe no permite crearlo solucita otro nombre usuario
@app.route('/create', methods = ['GET', 'POST'])
def create():
	create_form = forms.CreateForm(request.form)
	if request.method == 'POST' and create_form.validate():
		
		user = User(create_form.username.data,
					create_form.nombre.data,
					create_form.apellido.data,
					create_form.email.data,
					create_form.password.data)

		db.session.add(user)
		db.session.commit()
		success_message = 'Usuario registrado en la base de datos'
		flash(success_message)
		return redirect( url_for('logout') )
		
	return render_template('create.html', form = create_form)

#aplicacion que crea los comentarios y los salva en la base de datos segun la relacion existente
@app.route('/comment', methods = ['GET', 'POST'])
def comment():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		
		user_id = session['user_id']
		print(user_id)
		comment = Comment(user_id = user_id, 
						  text = comment_form.comment.data) 
		
		db.session.add(comment)
		db.session.commit()

		success_message = 'Nuevo Comentario Creado!'
		flash(success_message)

	title = "Comentarios"
	return render_template ('comment.html', title = title, form = comment_form )

#metodo que permite listar todos los usuarios y asi poderlos asignar a los 3 posibles equipos
@app.route('/usersteams', methods=['GET'])
def usersteams():
	usuarios = User.query.all()
	title = "Revision de Usuarios"
	return render_template('usersteams.html', title = title, usuarios = usuarios)

#lo usuarios se agregan a los respectivos teams, en este caso rojos, azules o verdes
@app.route('/teams/<int:id>/<string:color>') #recibe 2 variables el id del usuario y el equipo al que va a ser asignado
def teams(id,color):
	user = User.query.filter_by(id = id).first()
	ident = user.id
	nombreequipo = Teams(user_id = ident, nombre = color) 
	db.session.add(nombreequipo)
	db.session.commit()
	success_message = 'Usuario Agregado a Equipo!'
	flash(success_message)
	return redirect( url_for('usersteams') )

#lista todos los usuarios existentes en el equipo rojo, hace un join de 2 tablas y lo filtra por color.
@app.route('/usersred', methods=['GET'])
def usersred():
	redteams = Teams.query.join(User).add_columns( User.username, User.apellido, Teams.nombre).filter(Teams.nombre == 'ROJO')
	for redteam in redteams:
		print(redteam.username, redteam.apellido, redteam.nombre)
	title = "Listado Equipo Rojo"
	return render_template('usersred.html', title = title, redteams = redteams)

#lista todos los usuarios existentes en el equipo azul, hace un join de 2 tablas y lo filtra por color.
@app.route('/usersblue', methods=['GET'])
def usersblue():
	blueteams = Teams.query.join(User).add_columns( User.username, User.apellido, Teams.nombre).filter(Teams.nombre == 'AZUL')
	title = "Listado Equipo Azul"
	return render_template('usersblue.html', title = title, blueteams = blueteams)

#lista todos los usuarios existentes en el equipo verde, hace un join de 2 tablas y lo filtra por color.
@app.route('/usersgreen', methods=['GET'])
def usersgreen():
	greenteams = Teams.query.join(User).add_columns( User.username, User.apellido, Teams.nombre).filter(Teams.nombre == 'VERDE')
	title = "Listado Equipo Verde"
	return render_template('usersgreen.html', title = title, greenteams = greenteams)



#genera una tabla y lista todos los usuarios, la idea principal es poder borrar y modificar el mismo.
@app.route('/users', methods=['GET'])
def users():
	usuarios = User.query.all()
	for usuario in usuarios:
		print(usuario)
	title = "Revision de Usuarios"
	return render_template('users.html', title = title, usuarios = usuarios)

# genera una tabla con todos los comentatios generados por todos los usuarios sin importar a que team pertenece
@app.route('/reviews', methods=['GET'])
def reviews():
	comments = Comment.query.join(User).add_columns( User.username, Comment.text, Teams.nombre )
	title = "Revision de Comentarios"
	return render_template('reviews.html', title = title, comments = comments)

#funcion que prodece a actualizar el password del usuario. esta tarea se ejecuta desde el usuario superadmin, fecibe el id del usuario
@app.route('/update/<string:id>', methods = ['GET', 'POST'])
def update_user(id):
	user = User.query.filter_by(id = id).first()
	passw_form = forms.PassForm(request.form)
	if request.method == 'POST' and passw_form.validate():
		
		user.username = user.username
		user.nombre = user.nombre
		user.apellido =	user.apellido
		user.email = user.email
		user.password = generate_password_hash(passw_form.password.data)
		db.session.commit()
		return redirect( url_for('users') )
	return render_template('password.html', form = passw_form)


@app.route('/delete/<string:id>')
def delete_user(id): #este metodo borra al usuario, tenga o no comentarios y si tiene comentarios los borra tambien sin afectar los otros, recibe el id del usuario
	db.session.query(User).filter(User.id==id).delete()
	db.session.commit()
	success_message = 'Usuario borrado en la base de datos'
	flash(success_message)
	return redirect( url_for('users') )


@app.route('/ajax-login', methods=['POST'])
def ajax_login():
	username = request.form['username']
	response = {'status': 200, 'username': username, 'id': 1 }
	print(response)
	print(request.form)
	return json.dumps(response)

#genera la cookie, ayuda a manipular sesiones
@app.route('/cookie')
def cookie():
	response = make_response( render_template('cookie.html'))
	response.set_cookie('custome_cookie', 'Examen02')
	return response


if __name__=='__main__':
	csrf.init_app(app)
	db.init_app(app)

	with app.app_context():
		db.create_all()

	app.run(port=4000)


