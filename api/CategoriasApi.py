from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import app, db, ma

#llamamos al modelo de User
from models.CategoriasModel import Categoria, CategoriaSchema

ruta_categoria = Blueprint("route_categoria", __name__)

categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)

@ruta_categoria.route("/categoria", methods=["GET"])
def alluser():
    resultAll = Categoria.query.all()
    respo = categorias_schema(resultAll)
    return jsonify(respo)

@ruta_categoria.route("/registrarCategoria", methods=['POST'])
def registrarCategoria():
    imagenes= request.json['imagenes']
    nombre= request.json['nombre']
    newuser = Categoria(imagenes,nombre)
    db.session.add(newuser)
    db.session.commit()
    return "Guardado"

@ruta_categoria.route("eliminarCategoria", methods=['DELETE'])
def eliminarCategoria():
    id = request.json['id'] 
    categoria = Categoria.query.get(id)    
    db.session.delete(categoria)
    db.session.commit()     
    return jsonify(categoria_schema.dump(categoria))

