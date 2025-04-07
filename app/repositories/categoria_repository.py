from app.models.categoria import Categoria
from app import db
class CategoriaRepository:
    @staticmethod
    def get_all():
        return Categoria.query.all()

    @staticmethod
    def get_by_id(categoria_id):
        return Categoria.query.get(categoria_id)

    @staticmethod
    def create(categoria):
        db.session.add(categoria)
        db.session.commit()
        return categoria

    @staticmethod
    def update(categoria):
        db.session.commit()
        return categoria

    @staticmethod
    def delete(categoria):
        db.session.delete(categoria)
        db.session.commit()