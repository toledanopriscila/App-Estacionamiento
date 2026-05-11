from flask import request, redirect, url_for, session
from Models.vehiculo import Vehiculo
from Models.registro import Registro
from Models.configuracion import Configuracion
from Models import db
from datetime import datetime
import math

def registrar_entrada():
    u_id = session.get('usuario_id')
    vehiculo = Vehiculo.query.filter_by(usuario_id=u_id).first()
    if request.method == 'POST':
        nueva_entrada = Registro(vehiculo_id=vehiculo.id, hora_entrada=datetime.now())
        vehiculo.estado = 'dentro'
        db.session.add(nueva_entrada)
        db.session.commit()
        return f"Entrada registrada para: {vehiculo.patente}"
    return "Módulo de Entrada Activo"

def registrar_salida():
    if request.method == 'POST':
        patente = request.form.get('patente').strip()
        vehiculo = Vehiculo.query.filter_by(patente=patente).first()
        config = Configuracion.query.first()
        if vehiculo:
            reg = Registro.query.filter_by(vehiculo_id=vehiculo.id, hora_salida=None).first()
            if reg:
                reg.hora_salida = datetime.now()
                vehiculo.estado = 'fuera'
                dif = reg.hora_salida - reg.hora_entrada
                horas = max(1, math.ceil(dif.total_seconds() / 3600))
                total = horas * config.tarifa_hora
                db.session.commit()
                return f"SALIDA CONFIRMADA: Patente {patente} | Cobro: ${total}"
    return "Módulo de Salida Activo"
