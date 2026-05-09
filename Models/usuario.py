from Models import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    # Esto conecta al usuario con sus vehículos
    vehiculos = db.relationship('Vehiculo', backref='dueno', lazy=True)