from flask import Blueprint, request, jsonify
from backend.models.models import Product
from sqlalchemy import select, delete, update
from backend import db

bp = Blueprint("router", __name__)

def productExist(id):
    sql = select(Product).where(Product.id == id)
    product = db.session.execute(sql).scalar_one_or_none()

    if product:
        return True
    else:
        return False

@bp.route("/new", methods=["POST"])
def newProduct():
    data = request.get_json()

    name = data["name"]
    price = float(data["price"])
    qntd = int(data["qntd"])

    product = Product(name=name, price=price, qntd=qntd)

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "status": "success"
    })

@bp.route("/delete", methods=["DELETE"])
def deleteProduct():
    id = request.args.get("id")

    if not productExist(id):
        return jsonify({"error": "product doesnt exist"}), 401

    sql = delete(Product).where(Product.id == id)
    db.session.execute(sql)
    db.session.commit()

    return jsonify({"status": "success"})

@bp.route("/update", methods=["POST"])
def updateProduct():
    data = request.get_json()

    price = data["price"]
    qntd = data["qntd"]
    id = request.args.get("id")

    if not productExist(id):
        return jsonify({"error": "product doesnt exist"}), 401

    sql = update(Product).where(Product.id == id).values(price=price, qntd=qntd)
    db.session.execute(sql)

    db.session.commit()

    return jsonify({
        "status": "success"
    })

@bp.route("/get")
def getProducts():
    sql = select(Product)
    products = db.session.execute(sql).scalars()

    return jsonify([{"name": p.name, "price": p.price, "qntd": p.qntd} for p in products])

