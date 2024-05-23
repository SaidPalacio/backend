from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/AlquilerSillas'
user = "cristian"
password = "admin123"
direc = "cristian.mysql.pythonanywhere-services.com"
namebd = "cristian$AlquilerSillas"
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{direc}/{namebd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Alquiler"

db = SQLAlchemy(app)
ma = Marshmallow(app)