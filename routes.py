from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', subtitulo = "actividad del grupo de apps")

@app.route('/sobrenosotros')
def sobrenosotros():
    return render_template('sobrenosotros.html')
@app.route('/saludo')
def saludo():
    return 'bienvenidos a taller de apss'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'hola {nombre} bienvenido a taller de apss'