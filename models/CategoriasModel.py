from config.db import db, app, ma

class Categoria(db.Model):
    __tablename__ ='Categorias'

    id = db.Column(db.Integer, primary_key = True) 
    imagenes = db.Column(db.String(50))
    nombre = db.Column(db.String(50))

    def __init__(self, imagenes, nombre):
        self.imagenes = imagenes
        self.nombre = nombre
    
with app.app_context():
    db.create_all()
    
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('idcategorias','imagenes','nombre')

