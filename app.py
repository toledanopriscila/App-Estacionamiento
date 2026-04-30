from flask import Flask, render_template, redirect, url_for
from Config import Config
from Models import db
from Models.usuario import Usuario  
from Models.vehiculo import Vehiculo
from Models.registro import Registro
from Models.configuracion import Configuracion
from Models.metodo_pago import MetodoPago
from Router.configuracion_routes import config_bp
from Router.registro_routes import registro_bp
from Router.vehiculo_routes import vehiculo_bp
from Router.usuario_routes import usuario_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(usuario_bp)
app.register_blueprint(config_bp)
app.register_blueprint(registro_bp)
app.register_blueprint(vehiculo_bp)

# Inicializamos la base de datos con la configuración de tu .env
db.init_app(app)

@app.route('/')
def inicio():
    # Buscamos la configuración para saber el cupo total (ej: 50)
    config = Configuracion.query.first()
    
    # Contamos cuántos autos tienen estado 'dentro' en la base de datos
    autos_adentro = Vehiculo.query.filter_by(estado='dentro').count()
    
    # Hacemos la resta para saber cuántos quedan vacíos
    if config:
        libres = config.capacidad_maxima - autos_adentro
    else:
        libres = 0  # Si no hay configuración, por ahora decimos 0

    # Le pasamos el número "libres" a la pantalla del Dashboard
    return render_template('dashboard.html', libres=libres)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Esto crea las tablas si no existen
    app.run(debug=True)  # Esto mantiene el servidor encendido















