from Models import db

class Configuracion(db.Model):
    __tablename__ = 'configuracion'
    id = db.Column(db.Integer, primary_key=True)
    capacidad_maxima = db.Column(db.Integer, default=50)
    lugares_ocupados = db.Column(db.Integer, default=0)
    tarifa_hora = db.Column(db.Float, default=500.0)
    tarifa_media_estadia = db.Column(db.Float, default=2000.0) # Ejemplo 4hs
    tarifa_dia_completo = db.Column(db.Float, default=5000.0)
    
from flask import render_template, request, redirect, url_for
from Models import db
from Models.configuracion import Configuracion

def gestionar_tarifas():
    config = Configuracion.query.first()

    if request.method == 'POST':
        
        t_hora = request.form.get('tarifa_hora')
        t_media = request.form.get('tarifa_media_estadia')
        t_dia = request.form.get('tarifa_dia_completo')
        capacidad = request.form.get('capacidad_maxima')

        if not config:
            # Si no existe, creamos el registro con tus nombres de columna
            config = Configuracion(
                tarifa_hora=float(t_hora),
                tarifa_media_estadia=float(t_media),
                tarifa_dia_completo=float(t_dia),
                capacidad_maxima=int(capacidad)
            )
            db.session.add(config)
        else:
            # Si ya existe, actualizamos los valores
            config.tarifa_hora = float(t_hora)
            config.tarifa_media_estadia = float(t_media)
            config.tarifa_dia_completo = float(t_dia)
            config.capacidad_maxima = int(capacidad)
        
        db.session.commit()
        return redirect(url_for('inicio'))

    return render_template('tarifas.html', config=config)