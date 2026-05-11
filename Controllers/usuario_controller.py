from flask import request, redirect, url_for, session
from Models.usuario import Usuario
from Models import db

def registrar_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre').strip()
        apellido = request.form.get('apellido').strip()
        passw = request.form.get('contrasena').strip()
        nuevo = Usuario(nombre=nombre, apellido=apellido, contrasena=passw)
        db.session.add(nuevo)
        db.session.commit()
        return f"Usuario {nombre} guardado en DB. ID: {nuevo.id}"
    return "Módulo de Usuarios Activo"

def login_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre').strip()
        passw = request.form.get('contrasena').strip()
        user = Usuario.query.filter_by(nombre=nombre, contrasena=passw).first()
        if user:
            session['usuario_id'] = user.id
            session['usuario_nombre'] = user.nombre
            return f"Sesión iniciada para {user.nombre}"
    return "Login Activo"

def logout_usuario():
    session.clear()
    return redirect(url_for('usuario.login_usuario'))