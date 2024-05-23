from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import app, db, ma

#llamamos al modelo de User
from models.ProveedorModel import Proveedor, ProveeSchema

ruta_provee = Blueprint("route_provee", __name__)

proveedor_schema = ProveeSchema()
proveedors_schema = ProveeSchema(many=True)

@ruta_provee.route("/provee", methods=["GET"])
def alluser():
    resultAll = Proveedor.query.all()
    respo = proveedors_schema(resultAll)
    return jsonify(respo)

@ruta_provee.route("/registrarProveedor", methods=['POST'])
def registrarProveedor():
    nombre= request.json['nombre']
    apellido = request.json['apellido']
    direccion = request.json['direccion']
    telefono = request.json["telefono"]
    correo = request.json['correo']
    contrasena = request.json['contrasena']
    newuser = Proveedor(nombre, apellido, direccion, telefono, correo, contrasena)
    db.session.add(newuser)
    db.session.commit()
    return "Guardado"

@ruta_provee.route("eliminarProveedor", methods=['DELETE'])
def eliminarProveedor():
    id = request.json['id'] 
    proveedor = Proveedor.query.get(id)    
    db.session.delete(proveedor)
    db.session.commit()     
    return jsonify(proveedor_schema.dump(proveedor))

