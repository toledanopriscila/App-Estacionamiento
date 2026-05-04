from Models import db

class Configuracion(db.Model):
    __tablename__ = 'configuracion'
    id = db.Column(db.Integer, primary_key=True)
    capacidad_maxima = db.Column(db.Integer, default=50)
    lugares_ocupados = db.Column(db.Integer, default=0)
    tarifa_hora = db.Column(db.Float, default=500.0)
    tarifa_media_estadia = db.Column(db.Float, default=2000.0) # Ejemplo 4hs
    tarifa_dia_completo = db.Column(db.Float, default=5000.0)
    
    