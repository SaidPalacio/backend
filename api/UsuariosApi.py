from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import app, db, ma

#llamamos al modelo de User
from models.UsuariosModel import Users, UsersSchema

ruta_user = Blueprint("route_user", __name__)

usuario_schema = UsersSchema()
usuarios_schema = UsersSchema(many=True)

@ruta_user.route("/user", methods=["GET"])
def alluser():
    resultAll = Users.query.all()
    respo = usuarios_schema(resultAll)
    return jsonify(respo)

@ruta_user.route("/registrarUsuario", methods=['POST'])
def registrarUsuario():
    nombre= request.json['nombre']
    apellido = request.json['apellido']
    direccion = request.json['direccion']
    telefono = request.json["telefono"]
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    newuser = Users(nombre, apellido, direccion, telefono, correo, contrasena)
    db.session.add(newuser)
    db.session.commit()
    return "Guardado"

@ruta_user.route("eliminarUsuario", methods=['DELETE'])
def eliminarUsuario():
    id = request.json['id'] 
    usuario = Users.query.get(id)    
    db.session.delete(usuario)
    db.session.commit()     
    return jsonify(usuario_schema.dump(usuario))

