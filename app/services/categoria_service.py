from app.repositories.categoria_repository import CategoriaRepository
from app.schemas.categoria_schema import CategoriaCreate, CategoriaUpdate
from app.models.categoria import Categoria

class CategoriaService:
    @staticmethod
    def get_all_categorias():
        return CategoriaRepository.get_all()

    @staticmethod
    def get_categoria_by_id(categoria_id):
        return CategoriaRepository.get_by_id(categoria_id)

    @staticmethod
    def create_categoria(categoria: CategoriaCreate) -> Categoria:
        nueva_categoria = Categoria(**categoria.dict())
        return CategoriaRepository.create(nueva_categoria)

    @staticmethod
    def update_categoria(categoria_id: int, categoria_data: CategoriaUpdate) -> Categoria:
        categoria = CategoriaRepository.get_by_id(categoria_id)
        if not categoria:
            return None
        for key, value in categoria_data.dict(exclude_unset=True).items():
            setattr(categoria, key, value)
        return CategoriaRepository.update(categoria)

    @staticmethod
    def delete_categoria(categoria_id):
        categoria = CategoriaRepository.get_by_id(categoria_id)
        if not categoria:
            return None
        CategoriaRepository.delete(categoria)
        return True