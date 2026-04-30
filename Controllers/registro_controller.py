from flask import render_template, request, redirect, url_for
from Models.registro import Registro # Tu modelo Registro
from Models.vehiculo import Vehiculo # Tu modelo Vehiculo
from Models import db
from datetime import datetime

def registrar_entrada():
    if request.method == 'POST':
        patente = request.form.get('patente')
        vehiculo = Vehiculo.query.filter_by(patente=patente).first()

        if vehiculo:
            # Creamos el registro de entrada usando tu clase Registro
            nueva_entrada = Registro(vehiculo_id=vehiculo.id)
            vehiculo.estado = 'dentro' # Cambiamos el estado del vehículo
            
            db.session.add(nueva_entrada)
            db.session.commit()
            return redirect(url_for('inicio'))
            
    return render_template('entrada.html')

from Models.configuracion import Configuracion # Necesitamos los precios

def registrar_salida():
    if request.method == 'POST':
        patente = request.form.get('patente')
        # Buscamos el vehículo y su registro de entrada que no tenga hora de salida
        vehiculo = Vehiculo.query.filter_by(patente=patente).first()
        registro = Registro.query.filter_by(vehiculo_id=vehiculo.id, hora_salida=None).first()

        if registro:
            registro.hora_salida = datetime.now()
            # Calculamos el tiempo (en horas)
            diferencia = registro.hora_salida - registro.hora_entrada
            horas = diferencia.total_seconds() / 3600
            
            # Buscamos la tarifa actual
            config = Configuracion.query.first()
            precio_final = max(1, round(horas)) * config.tarifa_hora # Mínimo cobramos 1 hora
            
            registro.total_pago = precio_final
            vehiculo.estado = 'fuera'
            
            db.session.commit()
            return f"Salida registrada. Total a cobrar: ${precio_final}"
            
    return render_template('registro_salida.html')