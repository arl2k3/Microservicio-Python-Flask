from app.repositories.producto_repository import ProductoRepository
from app.schemas.producto_schema import ProductoCreate, ProductoUpdate
from app.models.producto import Producto

class ProductoService:
    @staticmethod
    def get_all_productos():
        return ProductoRepository.get_all()

    @staticmethod
    def get_producto_by_id(producto_id):
        return ProductoRepository.get_by_id(producto_id)

    @staticmethod
    def create_producto(producto: ProductoCreate) -> Producto:
        nuevo_producto = Producto(**producto.dict())
        return ProductoRepository.create(nuevo_producto)

    @staticmethod
    def update_producto(producto_id: int, producto_data: ProductoUpdate) -> Producto:
        producto = ProductoRepository.get_by_id(producto_id)
        if not producto:
            return None
        for key, value in producto_data.dict(exclude_unset=True).items():
            setattr(producto, key, value)
        return ProductoRepository.update(producto)

    @staticmethod
    def delete_producto(producto_id):
        producto = ProductoRepository.get_by_id(producto_id)
        if not producto:
            return None
        ProductoRepository.delete(producto)
        return True