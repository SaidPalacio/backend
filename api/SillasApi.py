from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import app, db, ma

# llamamos al modelo de Sillas
from models.SillasModel import Sillas, SillasSchema 

ruta_silla = Blueprint("route_silla", __name__)

sillas_schema = SillasSchema()
sillas_schemas = SillasSchema(many=True)

@ruta_silla.route("/sillas", methods=["GET"])
def all_sillas():
    resultAll = Sillas.query.all()
    respo = sillas_schemas(resultAll)
    return jsonify(respo)

@ruta_silla.route("/registrarSilla", methods=['POST'])
def registrar_silla():
    nombre = request.json['nombre']
    categoria = request.json['categoria']
    descripcion = request.json['descripcion']
    id = request.json['id']
    imagenes = request.json['imagenes']
    precio = request.json['precio']
    promocion = request.json['promocion']
    cantidad = request.json['cantidad']
    new_silla = Sillas(nombre, categoria, descripcion, id, imagenes, precio, promocion, cantidad)
    db.session.add(new_silla)
    db.session.commit()
    return "Guardado"

@ruta_silla.route("eliminarSilla", methods=['DELETE'])
def eliminar_silla():
    id = request.json['id'] 
    silla = Sillas.query.get(id)    
    db.session.delete(silla)
    db.session.commit()     
    return jsonify(sillas_schema.dump(silla))