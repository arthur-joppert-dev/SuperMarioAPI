from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
db = SQLAlchemy(app)
CORS(app)

from backend.models.models import Product
from backend.routes.router import bp

app.register_blueprint(bp)