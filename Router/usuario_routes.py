from flask import Blueprint
from Controllers.usuario_controller import registrar_usuario

# Creamos un Blueprint (es como un mapa de rutas)
usuario_bp = Blueprint('usuario', __name__)

# Definimos la ruta de registro
usuario_bp.route('/registro', methods=['GET', 'POST'])(registrar_usuario)