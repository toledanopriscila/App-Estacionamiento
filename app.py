from flask import Flask
from Config import Config
from Models import db
from Models.usuario import Usuario  
from Models.vehiculo import Vehiculo
from Models.registro import Registro
from Models.configuracion import Configuracion
from Models.metodo_pago import MetodoPago

app = Flask(__name__)
app.config.from_object(Config)

# Inicializamos la base de datos con la configuración de tu .env
db.init_app(app)

@app.route('/')
def inicio():
    return "¡API de Estacionamiento Funcionando!"

if __name__ == '__main__':
    with app.app_context():
        # Esto creará la tabla 'vehiculos' en tu Workbench automáticamente
        db.create_all()
    app.run(debug=True)















