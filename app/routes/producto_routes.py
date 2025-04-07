from flask import Blueprint
from app.controllers.producto_controller import ProductoController

producto_bp = Blueprint('producto', __name__)


producto_bp.route('/', methods=['GET'])(ProductoController.get_productos)
producto_bp.route('/<int:producto_id>', methods=['GET'])(ProductoController.get_producto)
producto_bp.route('/', methods=['POST'])(ProductoController.create_producto)
producto_bp.route('/<int:producto_id>', methods=['PUT'])(ProductoController.update_producto)
producto_bp.route('/<int:producto_id>', methods=['DELETE'])(ProductoController.delete_producto)