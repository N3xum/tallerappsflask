from app import app, db
from flask import render_template
import formularios
from models import Tareas
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', subtitulo = "actividad del grupo de apps")

@app.route('/sobrenosotros', methods=['GET', 'POST'])
def sobrenosotros():
    formulario = formularios.FormAgregarTareas()
    if formulario.validate_on_submit():
        nueva_tarea = Tareas(titulo = formulario.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()

        print(' envio correctamente', formulario.titulo.data)
        return render_template('sobrenosotros.html', 
                                form = formulario,
                                titulo = formulario.titulo.data)
    return render_template('sobrenosotros.html', form = formulario)
@app.route('/saludo')
def saludo():
    return 'bienvenidos a taller de apss'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'hola {nombre} bienvenido a taller de apss'