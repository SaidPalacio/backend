from config.db import db, app, ma

class Reserva(db.Model):
    __tablename__ = 'Reserva'

    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey("Usuarios.id"))
    idsilla = db.Column(db.Integer, db.ForeignKey("Sillas.id"))
    nombre = db.Column(db.String(50))
    categoria = db.Column(db.String(50))
    descripcion = db.Column(db.String(150))
    precio = db.Column(db.Double)
    promocion = db.Column(db.String(200))
    imagenes = db.Column(db.String(100))
    cantidad = db.Column(db.Integer(), default=0)
    def __init__(self,idusuario,idsilla, nombre, categoria, descripcion, precio, promocion, imagenes, cantidad):
        self.idusuario = idusuario
        self.idsilla = idsilla
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.precio = precio
        self.promocion = promocion
        self.imagenes = imagenes
        self.cantidad = cantidad

with app.app_context():
    db.create_all()

class ReservaSchema(ma.Schema):
    class Meta:
        fields = ('id','idusuario','idsilla', 'nombre', 'categoria', 'descripcion', 'precio', 'promocion', 'imagenes', 'cantidad')
