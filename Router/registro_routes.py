from flask import Blueprint
from Controllers.registro_controller import registrar_entrada

registro_bp = Blueprint('registro', __name__)

# Esta ruta será para marcar la entrada de un auto
registro_bp.route('/entrada', methods=['GET', 'POST'])(registrar_entrada)

from Controllers.registro_controller import registrar_salida 

registro_bp.route('/salida', methods=['GET', 'POST'])(registrar_salida)