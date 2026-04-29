from Models import db
from datetime import datetime

class Registro(db.Model):
    __tablename__ = 'registros'
    id = db.Column(db.Integer, primary_key=True)
    hora_entrada = db.Column(db.DateTime, default=datetime.now) # Se marca sola al entrar
    hora_salida = db.Column(db.DateTime, nullable=True) # Se llena al salir
    total_pago = db.Column(db.Float, default=0.0)
    metodo_pago = db.Column(db.String(50), nullable=True)
    
    # Conexión con el vehículo
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)