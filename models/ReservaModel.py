from config.db import db, app, ma

class Reserva(db.Model):
    __tablename__ = 'Reserva'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))##
    categoria = db.Column(db.String(50))##
    descripcion = db.Column(db.Text())##
    precio = db.Column(db.Float())##
    promocion = db.Column(db.String(200))##
    imagenes = db.Column(db.Text())##
    cantidad = db.Column(db.Integer(), default=0)##
    idusuario = db.Column(db.Integer, db.ForeignKey("Usuarios.id"))
    idsilla = db.Column(db.Integer, db.ForeignKey("Sillas.id"))

    def __init__(self, nombre, categoria, descripcion, precio, promocion, imagenes, cantidad, idusuario, idsilla):
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.precio = precio
        self.promocion = promocion
        self.imagenes = imagenes
        self.cantidad = cantidad
        self.idusuario = idusuario
        self.idsilla = idsilla

with app.app_context():
    db.create_all()

class ReservaSchema(ma.Schema):
    class Meta:
        fields = ('idsilla', 'nombre', 'categoria', 'descripcion', 'precio', 'promocion', 'imagenes', 'cantidad', 'idusuario', 'idsilla')