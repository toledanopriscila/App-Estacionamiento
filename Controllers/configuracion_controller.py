from flask import render_template, request, redirect, url_for
from Models.configuracion import Configuracion # Usamos tu modelo real
from Models import db

def gestionar_tarifas():
    # Buscamos la única configuración que existe
    config = Configuracion.query.first()

    if request.method == 'POST':
        if not config:
            config = Configuracion()
            db.session.add(config)
        
        config.tarifa_hora = float(request.form.get('tarifa_hora'))
        config.tarifa_media_estadia = float(request.form.get('tarifa_media_estadia'))
        config.tarifa_dia_completo = float(request.form.get('tarifa_dia_completo'))
        
        db.session.commit()
        return redirect(url_for('inicio'))

    return render_template('tarifas.html', config=config)