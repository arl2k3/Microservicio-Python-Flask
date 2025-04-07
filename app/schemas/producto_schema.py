from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    precio: float = Field(..., gt=0)
    categoria_id: int = Field(..., gt=0)

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    precio: Optional[float] = Field(None, gt=0)
    categoria_id: Optional[int] = Field(None, gt=0)

class ProductoResponse(ProductoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)