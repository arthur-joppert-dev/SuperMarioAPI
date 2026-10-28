from backend import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    qntd = db.Column(db.Integer)

