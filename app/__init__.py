from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Swagger(app)

    from app.routes.categoria_routes import categoria_bp
    from app.routes.producto_routes import producto_bp
    app.register_blueprint(categoria_bp, url_prefix='/api/categorias')
    app.register_blueprint(producto_bp, url_prefix='/api/productos')

    return app