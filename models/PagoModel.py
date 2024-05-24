from config.db import db, app, ma

class Pagos(db.Model):
    __tablename__ = 'Pagos'

    idpago = db.Column(db.Integer, primary_key=True)
    fechapago = db.Column(db.DateTime())
    idreserva = db.Column(db.String(50))
    metodopago = db.Column(db.String(50))
    monto = db.Column(db.Float())

    def __init__(self, fechapago, idreserva, metodopago, monto):
        self.fechapago = fechapago
        self.idreserva = idreserva
        self.metodopago = metodopago
        self.monto = monto

with app.app_context():
    db.create_all()

class PagosSchema(ma.Schema):
    class Meta:
        fields = ('idpago', 'fechapago', 'idreserva', 'metodopago', 'monto')