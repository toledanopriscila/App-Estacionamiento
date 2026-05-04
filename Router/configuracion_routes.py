from flask import Blueprint
from Controllers.configuracion_controller import gestionar_tarifas

config_bp = Blueprint('config', __name__)

# Esta es la ruta que fallaba porque no encontraba el nombre
config_bp.route('/tarifas', methods=['GET', 'POST'])(gestionar_tarifas)