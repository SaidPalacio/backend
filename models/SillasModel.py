from config.db import db, app, ma

class Sillas(db.Model):
    __tablename__ = 'Sillas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    categoria = db.Column(db.String(50))
    descripcion = db.Column(db.Text())
    precio = db.Column(db.Float())
    promocion = db.Column(db.Boolean(), default=False)
    imagenes = db.Column(db.Text())
    cantidad = db.Column(db.Integer(), default=0)

    def __init__(self, nombre, categoria, descripcion, precio, promocion, imagenes, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.precio = precio
        self.promocion = promocion
        self.imagenes = imagenes
        self.cantidad = cantidad

with app.app_context():
    db.create_all()

class SillasSchema(ma.Schema):
    class Meta:
        fields = ('idsilla', 'nombre', 'categoria', 'descripcion', 'precio', 'promocion', 'imagenes', 'cantidad')