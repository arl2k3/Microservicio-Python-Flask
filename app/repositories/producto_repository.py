from app.models.producto import Producto
from app import db
class ProductoRepository:
    @staticmethod
    def get_all():
        return Producto.query.all()

    @staticmethod
    def get_by_id(producto_id):
        return Producto.query.get(producto_id)

    @staticmethod
    def create(producto):
        db.session.add(producto)
        db.session.commit()
        return producto

    @staticmethod
    def update(producto):
        db.session.commit()
        return producto

    @staticmethod
    def delete(producto):
        db.session.delete(producto)
        db.session.commit()