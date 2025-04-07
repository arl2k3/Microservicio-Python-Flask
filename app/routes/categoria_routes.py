from flask import Blueprint
from app.controllers.categoria_controller import CategoriaController

categoria_bp = Blueprint('categoria', __name__)

categoria_bp.route('/', methods=['GET'])(CategoriaController.get_categorias)
categoria_bp.route('/<int:categoria_id>', methods=['GET'])(CategoriaController.get_categoria)
categoria_bp.route('/', methods=['POST'])(CategoriaController.create_categoria)
categoria_bp.route('/<int:categoria_id>', methods=['PUT'])(CategoriaController.update_categoria)
categoria_bp.route('/<int:categoria_id>', methods=['DELETE'])(CategoriaController.delete_categoria)