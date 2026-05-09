from flask import render_template, request, redirect, url_for, session
from Models.vehiculo import Vehiculo
from Models.registro import Registro
from Models.configuracion import Configuracion
from Models import db
from datetime import datetime
import math

def registrar_entrada():
    u_id = session.get('usuario_id')
    if not u_id:
        return redirect(url_for('usuario.login_usuario'))

    # Buscamos el vehículo del usuario logueado
    vehiculo = Vehiculo.query.filter_by(usuario_id=u_id).first()

    if not vehiculo:
        return "Primero debes cargar los datos de tu vehículo en el menú principal."

    if request.method == 'POST':
        # Registramos la entrada con la hora actual
        nueva_entrada = Registro(vehiculo_id=vehiculo.id, hora_entrada=datetime.now())
        vehiculo.estado = 'dentro'
        
        db.session.add(nueva_entrada)
        db.session.commit()
        return redirect(url_for('inicio'))
            
    return render_template('entrada.html', vehiculo=vehiculo)

def registrar_salida():
    if request.method == 'POST':
        patente = request.form.get('patente').strip()
        vehiculo = Vehiculo.query.filter_by(patente=patente).first()
        config = Configuracion.query.first()
        
        if vehiculo:
            registro = Registro.query.filter_by(vehiculo_id=vehiculo.id, hora_salida=None).first()
            if registro:
                ahora = datetime.now()
                registro.hora_salida = ahora
                vehiculo.estado = 'fuera'
                
                # Cálculo de tiempo y dinero
                diferencia = ahora - registro.hora_entrada
                horas_total = max(1, diferencia.total_seconds() / 3600)
                total_pagar = math.ceil(horas_total) * config.tarifa_hora
                
                db.session.commit()

                # Mandamos a la pantalla de ticket con estilo
                return render_template('cobro_detalle.html', 
                                       vehiculo=vehiculo, 
                                       total=total_pagar, 
                                       tiempo=round(horas_total, 2))
            
    return render_template('registro_salida.html')