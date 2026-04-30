from flask import Blueprint
from Controllers.configuracion_controller import gestionar_tarifas

config_bp = Blueprint('configuracion', __name__)

# Esta ruta será para ver y cambiar los precios
config_bp.route('/tarifas', methods=['GET', 'POST'])(gestionar_tarifas)