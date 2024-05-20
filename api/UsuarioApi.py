from flask import request, jsonify
from config.db import db, app, ma
from models.UsuarioModel import Usuario, UsuarioModelSchema

# Inicialización de esquemas
usuario_schema = UsuarioModelSchema()
usuarios_schema = UsuarioModelSchema(many=True)

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'GET':
        # Obtener todos los usuarios
        all_usuarios = Usuario.query.all()
        return jsonify(usuarios_schema.dump(all_usuarios))

    if request.method == 'POST':
        # Agregar un nuevo usuario
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
    user = Usuario.query.get(idusuario)
    if not user:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    if request.method == 'GET':
        # Obtener un usuario específico por ID
        return jsonify(usuario_schema.dump(user))

    if request.method == 'PUT':
        # Actualizar un usuario existente
        update_data = request.get_json()
        user.nombre = update_data.get('nombre', user.nombre)
        user.apellido = update_data.get('apellido', user.apellido)
        user.direccion = update_data.get('direccion', user.direccion)
        user.telefono = update_data.get('telefono', user.telefono)
        user.correo = update_data.get('correo', user.correo)
        user.contrasena = update_data.get('contrasena', user.contrasena)

        db.session.commit()
        return jsonify(usuario_schema.dump(user))

    if request.method == 'DELETE':
        # Eliminar un usuario por ID
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado'}), 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)
