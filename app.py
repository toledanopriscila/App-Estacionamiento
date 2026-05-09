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


app.secret_key = 'mi_clave_secreta_super_segura' 
app.config.from_object(Config)


app.register_blueprint(usuario_bp)
app.register_blueprint(config_bp)
app.register_blueprint(registro_bp)
app.register_blueprint(vehiculo_bp)

# Inicializamos la base de datos
db.init_app(app)

@app.route('/')
def inicio():
    # Buscamos la configuración para saber el cupo total 
    config = Configuracion.query.first()
    
    # Contamos cuántos autos tienen estado 'dentro'
    autos_adentro = Vehiculo.query.filter_by(estado='dentro').count()
    
    # Calculamos lugares libres
    if config:
        libres = config.capacidad_maxima - autos_adentro
    else:
        libres = 0

    return render_template('dashboard.html', libres=libres)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
