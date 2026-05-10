from flask import request, redirect, url_for
from Models.vehiculo import Vehiculo
from Models import db

def registrar_vehiculo():
    if request.method == 'POST':
        patente = request.form.get('patente')
        tipo = request.form.get('tipo')
        u_id = request.form.get('usuario_id')
        nuevo = Vehiculo(patente=patente, tipo=tipo, usuario_id=u_id)
        db.session.add(nuevo)
        db.session.commit()
        return f"Vehículo {patente} vinculado al usuario {u_id}"
    return "Módulo de Vehículos Activo"