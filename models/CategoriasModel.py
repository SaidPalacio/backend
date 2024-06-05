from config.db import db, app, ma

class Categoria(db.Model):
    __tablename__ ='Categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    imagenes = db.Column(db.String(255))  # Cambiar el tipo de datos a una cadena

    def __init__(self, nombre, imagenes):
        self.nombre = nombre
        self.imagenes = imagenes  # Asignar la lista de imágenes como una cadena

with app.app_context():
    db.create_all()

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('idcategorias', 'nombre', 'imagenes')
