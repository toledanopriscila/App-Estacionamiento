from flask import render_template, request, redirect, url_for, session
from Models.vehiculo import Vehiculo
from Models.registro import Registro
from Models.configuracion import Configuracion # Agregamos esto
from Models import db
from datetime import datetime
import math # Para redondear el tiempo

# ... (registrar_entrada queda igual) ...

def registrar_salida():
    if request.method == 'POST':
        patente = request.form.get('patente').strip()
        vehiculo = Vehiculo.query.filter_by(patente=patente).first()
        config = Configuracion.query.first() # Traemos las tarifas del admin
        
        if vehiculo:
            registro = Registro.query.filter_by(vehiculo_id=vehiculo.id, hora_salida=None).first()
            if registro:
                # 1. Marcamos la salida
                ahora = datetime.now()
                registro.hora_salida = ahora
                vehiculo.estado = 'fuera'
                
                # 2. CALCULAR TIEMPO (en horas)
                diferencia = ahora - registro.hora_entrada
                horas_total = diferencia.total_seconds() / 3600
                
                # Cobro mínimo de 1 hora si pasó menos tiempo
                if horas_total < 1:
                    horas_total = 1
                
                # 3. CALCULAR TOTAL
                # Usamos la tarifa_hora que cargaste en el panel de admin
                total_pagar = math.ceil(horas_total) * config.tarifa_hora
                
                db.session.commit()

                # 4. ENVIAR A LA PANTALLA DE COBRO (No al inicio)
                return render_template('cobro_detalle.html', 
                                       vehiculo=vehiculo, 
                                       total=total_pagar, 
                                       tiempo=round(horas_total, 2))
            
    return render_template('registro_salida.html')