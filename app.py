from flask import Flask
#crear instancia
app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)#para que actulice los cambios o reinicie


