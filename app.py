from flask import Flask
from extension import db
#crear instancia
app = Flask(__name__)
app.config['SECRET_KEY'] = 'scret1234'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/db_tareas"

# initialize the app with the extension
db.init_app(app)
from models import Tareas
with app.app_context():
    db.create_all()
from routes import *

if __name__ == '__main__':
    app.run(debug=True)#para que actulice los cambios o reinicie


