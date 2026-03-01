from flask import render_template, redirect, url_for, request
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
    todas_las_tareas = Tareas.query.all()
    return render_template('sobrenosotros.html', 
                                form = formulario,
                                tareas = todas_las_tareas,
                                titulo = formulario.titulo.data if formulario.validate_on_submit() else None)
    
    
@app.route('/saludo')
def saludo():
    return 'bienvenidos a taller de apss'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'hola {nombre} bienvenido a taller de apss'



# ELIMINAR - Vallejos Roberto 
@app.route('/eliminar/<int:id>')
def eliminar(id):
    
    tarea_a_eliminar = Tareas.query.get(id)
    
    
    if tarea_a_eliminar:
        db.session.delete(tarea_a_eliminar)
        db.session.commit()
        
    return redirect(url_for('sobrenosotros'))

# EDITAR - PETER CAMACHO
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
   
    tarea_a_editar = Tareas.query.get(id)
    
   
    formulario = formularios.FormAgregarTareas()
    
   
    if formulario.validate_on_submit():
        tarea_a_editar.titulo = formulario.titulo.data
        db.session.commit()
        
        return redirect(url_for('sobrenosotros'))
        
    
    elif request.method == 'GET':
        formulario.titulo.data = tarea_a_editar.titulo
        
    
    return render_template('editar.html', form=formulario, tarea=tarea_a_editar)