from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import app, db, ma

# llamamos al modelo de Sillas
from models.ReservaModel import Reserva, ReservaSchema 

ruta_reserva = Blueprint("route_reserva", __name__)

reservas_schema = ReservaSchema()
reservas_schemas = ReservaSchema(many=True)

@ruta_reserva.route("/reserva", methods=["GET"])
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
    new_reserva = Reserva(nombre, categoria, descripcion,imagenes, precio, promocion, cantidad)
    db.session.add(new_reserva)
    db.session.commit()
    return "Guardado"

@ruta_reserva.route("eliminarReserva", methods=['DELETE'])
def eliminar_reserva():
    id = request.json['id'] 
    reserva = Reserva.query.get(id)    
    db.session.delete(reserva)
    db.session.commit()     
    return jsonify(reservas_schema.dump(reserva))