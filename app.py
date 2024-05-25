from flask import Flask, request, redirect, render_template, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from config.db import app, db

# Trabajar en las rutas de blueprint con respecto a las API's
from api.UsuariosApi import ruta_user
from api.ProveedorApi import ruta_provee
from api.SillasApi import ruta_silla
from api.CategoriasApi import ruta_categoria
from api.ReservaApi import ruta_reserva
from api.PagoApi import ruta_pago

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'abcde'
jwt = JWTManager(app)

# Importar los Blueprints
app.register_blueprint(ruta_user, url_prefix="/api")
app.register_blueprint(ruta_provee, url_prefix="/api")
app.register_blueprint(ruta_silla, url_prefix="/api")
app.register_blueprint(ruta_categoria, url_prefix="/api")
app.register_blueprint(ruta_reserva, url_prefix="/api")
app.register_blueprint(ruta_pago, url_prefix="/api")

# Configurar el servidor
@app.route("/")
def index():
    return "hola"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
