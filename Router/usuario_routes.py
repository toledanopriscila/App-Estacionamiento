from flask import Blueprint
from Controllers.usuario_controller import registrar_usuario, login_usuario, logout_usuario

usuario_bp = Blueprint('usuario', __name__)

usuario_bp.route('/registro', methods=['GET', 'POST'])(registrar_usuario)
usuario_bp.route('/login', methods=['GET', 'POST'])(login_usuario)
usuario_bp.route('/logout')(logout_usuario)