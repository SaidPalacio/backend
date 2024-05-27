from flask import Flask, request, jsonify
from flask import Flask, request, redirect, render_template, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from config.db import app, db
from flask_cors import CORS
# Trabajar en las rutas de blueprint con respecto a las API's
from api.UsuariosApi import ruta_user
from api.ProveedorApi import ruta_provee
from api.SillasApi import ruta_silla
from api.CategoriasApi import ruta_categoria
from api.ReservaApi import ruta_reserva
from api.PagoApi import ruta_pago
from common.Token import generar_token, verificar_token

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'abcde'
jwt = JWTManager(app)
CORS(app)
# Importar los Blueprints
app.register_blueprint(ruta_user, url_prefix="/api")
app.register_blueprint(ruta_provee, url_prefix="/api")
app.register_blueprint(ruta_silla, url_prefix="/api")
app.register_blueprint(ruta_categoria, url_prefix="/api")
app.register_blueprint(ruta_reserva, url_prefix="/api")
app.register_blueprint(ruta_pago, url_prefix="/api")

@app.route('/obtenertoken', methods=["GET"])
def obtenertoken():
    datatoken = generar_token('Said', '123')
    var_token = datatoken['token']
    response = {
        "statusCode": 200,
        "body": var_token
    }
    return jsonify(response)

# Ruta para verificar el token
@app.route('/verificaciontoken', methods=["GET"])
def verificaciontoken():
    token = request.headers['Authorization']
    token = token.replace('Bearer ', "").replace("", "")
    vf = verificar_token(token)
    print(f"vf=>{vf}")
    return jsonify(vf)


# Configurar el servidor
@app.route("/")
def index():
    return "hola"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
