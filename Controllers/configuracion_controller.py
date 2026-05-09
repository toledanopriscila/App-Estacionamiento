from flask import render_template, request, redirect, url_for
from Models.configuracion import Configuracion
from Models import db

def gestionar_tarifas():
    # Buscamos la configuración (dueño del estacionamiento)
    config = Configuracion.query.first()

    if request.method == 'POST':
        # Usamos los nombres exactos que tenés en tu base de datos
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
                tarifa_hora=t_hora,
                tarifa_media_estadia=t_media,
                tarifa_dia_completo=t_dia,
                capacidad_maxima=capacidad
            )
            db.session.add(nueva_config)

        db.session.commit()
        return redirect(url_for('inicio'))

    # Renderiza la plantilla donde el admin carga los números
    return render_template('tarifas.html', config=config)