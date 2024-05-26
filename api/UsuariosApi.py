from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config.db import db
from models.UsuariosModel import Users, UsersSchema

ruta_user = Blueprint("ruta_user", __name__)

usuario_schema = UsersSchema()
usuarios_schema = UsersSchema(many=True)

@ruta_user.route("/user", methods=["GET"])
@jwt_required()
def alluser():
    resultAll = Users.query.all()
    respo = usuarios_schema.dump(resultAll)
    return jsonify(respo)

@ruta_user.route("/registrarUsuario", methods=['POST'])
def registrarUsuario():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    correo = request.json['correo']
    contrasena = generate_password_hash(request.json['contrasena'])
    newuser = Users(nombre, apellido, direccion, telefono, correo, contrasena)
    db.session.add(newuser)
    db.session.commit()
    return "Guardado"

@ruta_user.route("/login", methods=['POST'])
def login():
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    user = Users.query.filter_by(correo=correo).first()
    if user and check_password_hash(user.contrasena, contrasena):
        access_token = create_access_token(identity={'id': user.id, 'correo': user.correo})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

@ruta_user.route("/eliminarUsuario", methods=['DELETE'])
@jwt_required()
def eliminarUsuario():
    id = request.json['id']
    usuario = Users.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(usuario_schema.dump(usuario))
