from Models import db

class Vehiculo(db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, primary_key=True)
    patente = db.Column(db.String(20), unique=True, nullable=False) # 'unique' evita duplicados
    tipo = db.Column(db.String(20), nullable=False) # Auto o Moto
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    estado = db.Column(db.String(20), default='fuera') # 'dentro' o 'fuera'