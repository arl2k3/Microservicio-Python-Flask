from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)

class CategoriaResponse(CategoriaBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)