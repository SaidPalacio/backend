from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config.db import app, db, ma

# llamamos al modelo de Sillas
from models.SillasModel import Sillas, SillasSchema 

ruta_silla = Blueprint("route_silla", __name__)

sillas_schema = SillasSchema()
sillas_schemas = SillasSchema(many=True)

@ruta_silla.route("/sillas", methods=["GET"])
@jwt_required()
def all_sillas():
    resultAll = Sillas.query.all()
    respo = sillas_schemas(resultAll)
    return jsonify(respo)

@ruta_silla.route("/registrarSilla", methods=['POST'])
def registrar_silla():
    nombre = request.json['nombre']
    categoria = request.json['categoria']
    descripcion = request.json['descripcion']
    imagenes = request.json['imagenes']
    precio = request.json['precio']
    promocion = request.json['promocion']
    cantidad = request.json['cantidad']
    new_silla = Sillas(nombre, categoria, descripcion, precio, promocion, imagenes, cantidad)
    db.session.add(new_silla)
    db.session.commit()
    return "Guardado"

@ruta_silla.route("/sillaCreada", methods=['POST'])
def silla_creada():
    nombre = request.json['nombre']
    silla = Sillas.query.filter_by(nombre=nombre).first()
    if silla:
        return jsonify({"msg": "Silla encontrada", "silla": silla.serialize()})
    return jsonify({"msg": "Silla no encontrada"}), 404
    
@ruta_silla.route("/Obtenersillas", methods=["GET"])
def get_all_sillas():
    try:
        # Consulta todas las sillas en la base de datos
        sillas = Sillas.query.all()

        # Serializa las sillas a un formato JSON
        sillas_json = []
        for silla in sillas:
            silla_data = {
                "id": silla.id,
                "nombre": silla.nombre,
                "categoria": silla.categoria,
                "descripcion": silla.descripcion,
                "precio": silla.precio,
                "promocion": silla.promocion,
                "imagenes": silla.imagenes,
                "cantidad": silla.cantidad
            }
            sillas_json.append(silla_data)

        # Devuelve la lista de sillas en formato JSON
        return jsonify(sillas_json), 200
    except Exception as e:
        # En caso de error, devuelve un mensaje de error
        return jsonify({"message": "Error al obtener las sillas", "error": str(e)}), 500


@ruta_silla.route("eliminarSilla", methods=['DELETE'])
@jwt_required()
def eliminar_silla():
    id = request.json['id'] 
    silla = Sillas.query.get(id)    
    db.session.delete(silla)
    db.session.commit()     
    return jsonify(sillas_schema.dump(silla))