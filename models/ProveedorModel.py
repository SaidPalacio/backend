from config.db import db, app, ma

class Proveedor(db.Model):
    __tablename__ ='Proveedores'

    id = db.Column(db.Integer, primary_key = True) 
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(50))
    contrasena = db.Column(db.String(255))

    def __init__(self, nombre, apellido, direccion, telefono, correo, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
    
with app.app_context():
    db.create_all()
    
class ProveeSchema(ma.Schema):
    class Meta:
        fields = ('idusuario', 'nombre', 'apellido', 'direccion', 'telefono', 'correo', 'contrasena')

