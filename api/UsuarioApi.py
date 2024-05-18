from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from config.db import db, app, ma
from marshmallow import fields

# Define the UsuarioModelSchema using Marshmallow
class UsuarioModelSchema(ma.Schema):
    class Meta:
        fields = ('idusuario', 'nombre', 'apellido', 'direccion', 'telefono', 'correo', 'contrasena')

    idusuario = fields.Int(dump_only=True)  # Set idusuario as read-only
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    direccion = fields.Str()
    telefono = fields.Str()
    correo = fields.Str(required=True)
    contrasena = fields.Str(required=True)

# Initialize the Marshmallow schema
usuario_schema = UsuarioModelSchema()
usuarios_schema = UsuarioModelSchema(many=True)  # For multiple users

# Import the Usuario model
from app.models import Usuario # type: ignore


@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'GET':
        # Get all users
        all_usuarios = Usuario.query.all()
        return jsonify(usuarios_schema.dump(all_usuarios))

    # Add a new user
    if request.method == 'POST':
        new_user_data = request.get_json()
        new_user = Usuario(
            nombre=new_user_data['nombre'],
            apellido=new_user_data['apellido'],
            direccion=new_user_data.get('direccion'),
            telefono=new_user_data.get('telefono'),
            correo=new_user_data['correo'],
            contrasena=new_user_data['contrasena']
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(usuario_schema.dump(new_user)), 201  # Created status code

@app.route('/usuarios/<int:idusuario>', methods=['GET', 'PUT', 'DELETE'])
def usuario_by_id(idusuario):
    if request.method == 'GET':
        # Get a specific user by ID
        user = Usuario.query.get(idusuario)
        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404  # Not Found

        return jsonify(usuario_schema.dump(user))

    if request.method == 'PUT':
        # Update an existing user
        user = Usuario.query.get(idusuario)
        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        update_data = request.get_json()
        user.nombre = update_data.get('nombre') or user.nombre
        user.apellido = update_data.get('apellido') or user.apellido
        user.direccion = update_data.get('direccion') or user.direccion
        user.telefono = update_data.get('telefono') or user.telefono
        user.correo = update_data.get('correo') or user.correo
        user.contrasena = update_data.get('contrasena') or user.contrasena

        db.session.commit()
        return jsonify(usuario_schema.dump(user))

    if request.method == 'DELETE':
        # Delete a user by ID
        user = Usuario.query.get(idusuario)
        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'Usuario eliminado'}), 204  # No Content
