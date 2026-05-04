from flask import render_template, request, redirect, url_for, flash
from Models.vehiculo import Vehiculo
from Models import db

def registrar_vehiculo():
    # Capturamos el ID del usuario que viene del registro anterior
    u_id = request.args.get('usuario_id') 
    
    if request.method == 'POST':
        patente = request.form.get('patente')
        tipo = request.form.get('tipo')
        propietario_id = request.form.get('usuario_id') 

        nuevo_vehiculo = Vehiculo(patente=patente, tipo=tipo, usuario_id=propietario_id)

        try:
            db.session.add(nuevo_vehiculo)
            db.session.commit()
            return redirect(url_for('inicio')) 
        except Exception as e:
            db.session.rollback()
            # Cambié el mensaje de error aquí:
            return f"Error al cargar datos: {e}"

    return render_template('registro_vehiculo.html', usuario_id=u_id)