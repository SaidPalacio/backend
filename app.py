from flask import Flask, request, redirect, render_template
from config.db import app

# trabajar en las rutas de bluprint con respectos a las api's
from api.UsuariosApi import ruta_user
from api.ProveedorApi import ruta_provee
from api.SillasApi import ruta_silla
from api.CategoriasApi import ruta_categoria
from api.ReservaApi import ruta_reserva
from api.PagoApi import ruta_pago

# Importar los Blueprints
app.register_blueprint(ruta_user, url_prefix="/api")
app.register_blueprint(ruta_provee, url_prefix="/api")
app.register_blueprint(ruta_silla, url_prefix="/api")
app.register_blueprint(ruta_categoria, url_prefix="/api")
app.register_blueprint(ruta_reserva, url_prefix="/api")
app.register_blueprint(ruta_pago, url_prefix="/api")

# config el servidor


@app.route("/")
def index():
    return "hola"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
