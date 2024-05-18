from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tasksul'
user = "winsignares"
password = "admin123"
direc = "winsignares.mysql.pythonanywhere-services.com"
namebd = "winsignares$tasksul"
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{direc}/{namebd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Movil2"


db = SQLAlchemy(app)
ma = Marshmallow(app)