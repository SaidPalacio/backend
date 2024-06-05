from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config.db import app, db, ma
from common.routeProtection import token_required

# llamamos al modelo de Sillas
from models.ReservaModel import Reserva, ReservaSchema

ruta_reserva = Blueprint("route_reserva", __name__)

reservas_schema = ReservaSchema()
reservas_schemas = ReservaSchema(many=True)

@ruta_reserva.route("/reserva", methods=["GET"])
#@jwt_required()
def all_reservas():
    resultAll = Reserva.query.all()
    respo = reservas_schemas(resultAll)
    return jsonify(respo)

@ruta_reserva.route("/registrarReserva", methods=['POST'])
@token_required
def registrar_reserva():
    idusuario = request.json['idusuario']
    idsilla = request.json['idsilla']
    nombre = request.json['nombre']
    categoria = request.json['categoria']
    descripcion = request.json['descripcion']
    precio = request.json['precio']
    promocion = request.json['promocion']
    imagenes = request.json['imagenes']
    cantidad = request.json['cantidad']
    new_reserva = Reserva(idusuario,idsilla,nombre,categoria,descripcion,precio,promocion,imagenes,cantidad)
    db.session.add(new_reserva)
    db.session.commit()
    return "Guardado"

@ruta_reserva.route("/ObtenerReservas", methods=["GET"])
@token_required
def get_all_reservas():
    try:
        # Obtener el idusuario desde los parámetros de la solicitud
        idusuario = request.args.get('idusuario')

        # Validar si idusuario fue proporcionado
        if not idusuario:
            return jsonify({"message": "idusuario es requerido"}), 400

        # Consulta las reservas en la base de datos filtradas por idusuario
        reservas = Reserva.query.filter_by(idusuario=idusuario).all()

        # Serializa las reservas a un formato JSON
        reservas_json = []
        for reserva in reservas:
            reserva_data = {
                "id": reserva.id,
                "idusuario": reserva.idusuario,
                "idsilla": reserva.idsilla,
                "nombre": reserva.nombre,
                "categoria": reserva.categoria,
                "descripcion": reserva.descripcion,
                "precio": reserva.precio,
                "promocion": reserva.promocion,
                "imagenes": reserva.imagenes,
                "cantidad": reserva.cantidad
            }
            reservas_json.append(reserva_data)

        # Devuelve la lista de reservas en formato JSON
        return jsonify(reservas_json), 200
    except Exception as e:
        # En caso de error, devuelve un mensaje de error
        return jsonify({"message": "Error al obtener las reservas", "error": str(e)}), 500

@ruta_reserva.route("/ObtenerReservasss", methods=["GET"])
def get_all_reservasss():
    try:
        # Consulta todas las reservas en la base de datos
        reservas = Reserva.query.all()

        # Serializa las reservas a un formato JSON
        reservas_json = []
        for reserva in reservas:
            reserva_data = {
                "id": reserva.id,
                "idusuario":reserva.idusuario,
                "idsilla":reserva.idsilla,
                "nombre": reserva.nombre,
                "categoria": reserva.categoria,
                "descripcion": reserva.descripcion,
                "precio": reserva.precio,
                "promocion": reserva.promocion,
                "imagenes": reserva.imagenes,
                "cantidad": reserva.cantidad
            }
            reservas_json.append(reserva_data)

        # Devuelve la lista de reservas en formato JSON
        return jsonify(reservas_json), 200
    except Exception as e:
        # En caso de error, devuelve un mensaje de error
        return jsonify({"message": "Error al obtener las reservas", "error": str(e)}), 500



@ruta_reserva.route("eliminarReserva", methods=['DELETE'])
#@jwt_required()
def eliminar_reserva():
    id = request.json['id']
    reserva = Reserva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify(reservas_schema.dump(reserva))