from flask import request, redirect, url_for
from Models.configuracion import Configuracion
from Models import db

def gestionar_tarifas():
    config = Configuracion.query.first()
    if request.method == 'POST':
        t_hora = float(request.form.get('tarifa_hora'))
        t_media = float(request.form.get('tarifa_media'))
        t_dia = float(request.form.get('tarifa_dia'))
        capacidad = int(request.form.get('capacidad'))

        if config:
            config.tarifa_hora = t_hora
            config.tarifa_media_estadia = t_media
            config.tarifa_dia_completo = t_dia
            config.capacidad_maxima = capacidad
        else:
            nueva_config = Configuracion(
                tarifa_hora=t_hora, tarifa_media_estadia=t_media,
                tarifa_dia_completo=t_dia, capacidad_maxima=capacidad
            )
            db.session.add(nueva_config)
        db.session.commit()
        return "Configuración guardada en la base de datos con éxito."

    return "Esperando datos de configuración..."