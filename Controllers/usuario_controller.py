from flask import render_template, request, redirect, url_for, flash
from Models.usuario import Usuario
from Models import db

def registrar_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        contrasena = request.form.get('contrasena')

        # Creamos el nuevo usuario
        nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, contrasena=contrasena)
        
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            return redirect(url_for('inicio')) # Después de registrar, lo mandamos al login
        except Exception as e:
            db.session.rollback()
            return f"Error al registrar: {e}"

    return render_template('registro.html')