from flask import render_template, request, redirect, url_for, session
from Models.usuario import Usuario
from Models import db

def registrar_usuario():
    if request.method == 'POST':
        # Limpiamos espacios al registrar
        nombre = request.form.get('nombre').strip()
        apellido = request.form.get('apellido').strip()
        contrasena = request.form.get('contrasena').strip()

        nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, contrasena=contrasena)
        
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            # Te manda a cargar el vehículo pasando el ID
            return redirect(url_for('vehiculo.registrar_vehiculo', usuario_id=nuevo_usuario.id))
        except Exception as e:
            db.session.rollback()
            return f"Error al registrar: {e}"

    return render_template('registro.html')

def login_usuario():
    if request.method == 'POST':
        # Limpiamos espacios al iniciar sesión
        nombre_ingresado = request.form.get('nombre').strip()
        contrasena_ingresada = request.form.get('contrasena').strip()

        # Buscamos al usuario por nombre
        usuario = Usuario.query.filter_by(nombre=nombre_ingresado).first()

        # Verificamos si existe y si la contraseña coincide exactamente
        if usuario and usuario.contrasena == contrasena_ingresada:
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            return redirect(url_for('inicio'))
        else:
            return "Usuario o contraseña incorrectos. Revisá si usaste mayúsculas."

    return render_template('login.html')

def logout_usuario():
    session.clear()
    return redirect(url_for('inicio'))