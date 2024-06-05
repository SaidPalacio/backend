from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config.db import app, db, ma
from models.CategoriasModel import Categoria, CategoriaSchema
from common.routeProtection import token_required


app.config['JWT_SECRET_KEY'] = 'tusecretomuyseguro'
ruta_categoria = Blueprint("route_categoria", __name__)

categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)

@ruta_categoria.route("/categoria", methods=["GET"])
@jwt_required()
def alluser():
    resultAll = Categoria.query.all()
    respo = categorias_schema(resultAll)
    return jsonify(respo)

@ruta_categoria.route("/registrarCategoriaaa", methods=['POST'])
@token_required
def registrarCategoriaaa():
    imagenes= request.json['imagenes']
    nombre= request.json['nombre']
    newuser = Categoria(nombre,imagenes)
    db.session.add(newuser)
    db.session.commit()
    return "Guardado"

@ruta_categoria.route("/Obtenercategorias", methods=["GET"])
#@token_required
def get_all_categorias():
    try:
        # Consulta todas las categorias en la base de datos
        categorias = Categoria.query.all()

        # Serializa las sillas a un formato JSON
        categorias_json = []
        for categoria in categorias:
            categoria_data = {
                "id": categoria.id,
                "nombre": categoria.nombre,
                "imagenes": categoria.imagenes,
            }
            categorias_json.append(categoria_data)

        # Devuelve la lista de categorias en formato JSON
        return jsonify(categorias_json), 200
    except Exception as e:
        # En caso de error, devuelve un mensaje de error
        return jsonify({"message": "Error al obtener las categorias", "error": str(e)}), 500


@ruta_categoria.route("eliminarCategoria", methods=['DELETE'])
def eliminarCategoria():
    id = request.json['id']
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify(categoria_schema.dump(categoria))

