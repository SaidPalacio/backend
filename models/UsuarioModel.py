from config.db import db, app, ma

class Usuario(db.Model):
    __tablename__ ='tblusuario'

idusuario = db.Column(db.Integer, primary_key=True) 
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

def __str__(self):
    
    return f"Usuario: {self.nombre} {self.apellido} - Dirección: {self.direccion} - Teléfono: {self.telefono} - Correo: {self.correo}"  


with app.app_context():
  db.create_all()  # Crea las tablas si no existen


class UsuarioModelSchema(ma.Schema):
  class Meta:
    fields = ('idusuario', 'nombre', 'apellido', 'direccion', 'telefono', 'correo', 'contrasena')  