from flask import Blueprint
from Controllers.vehiculo_controller import registrar_vehiculo

vehiculo_bp = Blueprint('vehiculo', __name__)

# Esta ruta es para dar de alta un auto nuevo en el sistema
vehiculo_bp.route('/registrar_vehiculo', methods=['GET', 'POST'])(registrar_vehiculo)