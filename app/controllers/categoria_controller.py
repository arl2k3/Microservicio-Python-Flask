from flask import jsonify, request
from app.services.categoria_service import CategoriaService
from app.schemas.categoria_schema import CategoriaCreate, CategoriaUpdate
from flasgger import swag_from
from pydantic import ValidationError

class CategoriaController:
    @staticmethod
    @swag_from({
        'responses': {
            200: {
                'description': 'Lista de categorías',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'nombre': {'type': 'string'},
                            'descripcion': {'type': 'string', 'nullable': True},
                            'created_at': {'type': 'string', 'format': 'date-time'},
                            'updated_at': {'type': 'string', 'format': 'date-time'}
                        }
                    }
                }
            }
        }
    })
    def get_categorias():
        categorias = CategoriaService.get_all_categorias()
        return jsonify([cat.to_dict() for cat in categorias])

    @staticmethod
    @swag_from({
        'parameters': [
            {
                'name': 'categoria_id',
                'in': 'path',
                'type': 'integer',
                'required': True
            }
        ],
        'responses': {
            200: {'description': 'Categoría encontrada'},
            404: {'description': 'Categoría no encontrada'}
        }
    })
    def get_categoria(categoria_id: int):
        categoria = CategoriaService.get_categoria_by_id(categoria_id)
        if not categoria:
            return jsonify({'error': 'Categoría no encontrada'}), 404
        return jsonify(categoria.to_dict())

    @staticmethod
    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': CategoriaCreate.schema()
            }
        ],
        'responses': {
            201: {'description': 'Categoría creada'},
            422: {'description': 'Datos inválidos'}
        }
    })
    def create_categoria():
        try:
            data = request.get_json()
            categoria = CategoriaCreate(**data)
            nueva_categoria = CategoriaService.create_categoria(categoria)
            return jsonify({'message': 'Categoría creada', 'categoria': nueva_categoria.to_dict()}), 201
        except ValidationError as e:
            return jsonify({'error': e.errors()}), 422

    @staticmethod
    @swag_from({
        'parameters': [
            {
                'name': 'categoria_id',
                'in': 'path',
                'type': 'integer',
                'required': True
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': CategoriaUpdate.schema()
            }
        ],
        'responses': {
            200: {'description': 'Categoría actualizada'},
            404: {'description': 'Categoría no encontrada'},
            422: {'description': 'Datos inválidos'}
        }
    })
    def update_categoria(categoria_id: int):
        try:
            data = request.get_json()
            categoria_data = CategoriaUpdate(**data)
            updated_categoria = CategoriaService.update_categoria(categoria_id, categoria_data)
            if not updated_categoria:
                return jsonify({'error': 'Categoría no encontrada'}), 404
            return jsonify({'message': 'Categoría actualizada', 'categoria': updated_categoria.to_dict()})
        except ValidationError as e:
            return jsonify({'error': e.errors()}), 422

    @staticmethod
    @swag_from({
        'parameters': [
            {
                'name': 'categoria_id',
                'in': 'path',
                'type': 'integer',
                'required': True
            }
        ],
        'responses': {
            200: {'description': 'Categoría eliminada'},
            404: {'description': 'Categoría no encontrada'}
        }
    })
    def delete_categoria(categoria_id: int):
        deleted = CategoriaService.delete_categoria(categoria_id)
        if not deleted:
            return jsonify({'error': 'Categoría no encontrada'}), 404
        return jsonify({'message': 'Categoría eliminada'})