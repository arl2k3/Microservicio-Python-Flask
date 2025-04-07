from flask import jsonify, request
from app.services.producto_service import ProductoService
from app.schemas.producto_schema import ProductoCreate, ProductoUpdate
from flasgger import swag_from
from pydantic import ValidationError

class ProductoController:
    @staticmethod
    @swag_from({
        'responses': {
            200: {
                'description': 'Lista de productos',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'nombre': {'type': 'string'},
                            'precio': {'type': 'number'},
                            'categoria_id': {'type': 'integer'},
                            'created_at': {'type': 'string', 'format': 'date-time'},
                            'updated_at': {'type': 'string', 'format': 'date-time'}
                        }
                    }
                }
            }
        }
    })
    def get_productos():
        productos = ProductoService.get_all_productos()
        return jsonify([prod.to_dict() for prod in productos])

    @staticmethod
    @swag_from({
        'parameters': [
            {
                'name': 'producto_id',
                'in': 'path',
                'type': 'integer',
                'required': True
            }
        ],
        'responses': {
            200: {'description': 'Producto encontrado'},
            404: {'description': 'Producto no encontrado'}
        }
    })
    def get_producto(producto_id: int):
        producto = ProductoService.get_producto_by_id(producto_id)
        if not producto:
            return jsonify({'error': 'Producto no encontrado'}), 404
        return jsonify(producto.to_dict())

    @staticmethod
    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': ProductoCreate.schema()
            }
        ],
        'responses': {
            201: {'description': 'Producto creado'},
            422: {'description': 'Datos inválidos'}
        }
    })
    def create_producto():
        try:
            data = request.get_json()
            producto = ProductoCreate(**data)
            nuevo_producto = ProductoService.create_producto(producto)
            return jsonify({'message': 'Producto creado', 'producto': nuevo_producto.to_dict()}), 201
        except ValidationError as e:
            return jsonify({'error': e.errors()}), 422

    @staticmethod
    @swag_from({
        'parameters': [
            {
                'name': 'producto_id',
                'in': 'path',
                'type': 'integer',
                'required': True
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': ProductoUpdate.schema()
            }
        ],
        'responses': {
            200: {'description': 'Producto actualizado'},
            404: {'description': 'Producto no encontrado'},
            422: {'description': 'Datos inválidos'}
        }
    })
    def update_producto(producto_id: int):
        try:
            data = request.get_json()
            producto_data = ProductoUpdate(**data)
            updated_producto = ProductoService.update_producto(producto_id, producto_data)
            if not updated_producto:
                return jsonify({'error': 'Producto no encontrado'}), 404
            return jsonify({'message': 'Producto actualizado', 'producto': updated_producto.to_dict()})
        except ValidationError as e:
            return jsonify({'error': e.errors()}), 422

    @staticmethod
    @swag_from({
        'parameters': [
            {
                'name': 'producto_id',
                'in': 'path',
                'type': 'integer',
                'required': True
            }
        ],
        'responses': {
            200: {'description': 'Producto eliminado'},
            404: {'description': 'Producto no encontrado'}
        }
    })
    def delete_producto(producto_id: int):
        deleted = ProductoService.delete_producto(producto_id)
        if not deleted:
            return jsonify({'error': 'Producto no encontrado'}), 404
        return jsonify({'message': 'Producto eliminado'})