from flask import Flask, Blueprint, request, jsonify
from config.db import app, db, ma

# llamamos al modelo de Pagos
from models.PagoModel import Pagos, PagosSchema 

ruta_pago = Blueprint("route_pago", __name__)

pago_schema = PagosSchema()
pagos_schemas = PagosSchema(many=True)

@ruta_pago.route("/pagos", methods=["GET"])
def all_pagos():
    resultAll = Pagos.query.all()
    respo = pagos_schemas.dump(resultAll)
    return jsonify(respo)

@ruta_pago.route("/registrarPago", methods=['POST'])
def registrar_pago():
    fechapago = request.json['fechapago']
    idreserva = request.json['idreserva']
    metodopago = request.json['metodopago']
    monto = request.json['monto']
    new_pago = Pagos(fechapago, idreserva, metodopago, monto)
    db.session.add(new_pago)
    db.session.commit()
    return "Pago registrado"

@ruta_pago.route("/eliminarPago", methods=['DELETE'])
def eliminar_pago():
    idpago = request.json['idpago'] 
    pago = Pagos.query.get(idpago)    
    db.session.delete(pago)
    db.session.commit()     
    return jsonify(pago_schema.dump(pago))