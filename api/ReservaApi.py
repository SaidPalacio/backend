from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config.db import app, db, ma

# llamamos al modelo de Sillas
from models.ReservaModel import Reserva, ReservaSchema 

ruta_reserva = Blueprint("route_reserva", __name__)

reservas_schema = ReservaSchema()
reservas_schemas = ReservaSchema(many=True)

@ruta_reserva.route("/reserva", methods=["GET"])
@jwt_required()
def all_reservas():
    resultAll = Reserva.query.all()
    respo = reservas_schemas(resultAll)
    return jsonify(respo)

@ruta_reserva.route("/registrarReserva", methods=['POST'])

def registrar_reserva():
    nombre = request.json['nombre']
    categoria = request.json['categoria']
    descripcion = request.json['descripcion']
    imagenes = request.json['imagenes']
    precio = request.json['precio']
    promocion = request.json['promocion']
    cantidad = request.json['cantidad']
    idusuario = request.json['idusuario']
    idsilla = request.json['idsilla']
    new_reserva = Reserva(nombre, categoria, descripcion,imagenes, precio, promocion, cantidad, idusuario, idsilla)
    db.session.add(new_reserva)
    db.session.commit()
    return "Guardado"

@ruta_reserva.route("eliminarReserva", methods=['DELETE'])
@jwt_required()
def eliminar_reserva():
    id = request.json['id'] 
    reserva = Reserva.query.get(id)    
    db.session.delete(reserva)
    db.session.commit()     
    return jsonify(reservas_schema.dump(reserva))