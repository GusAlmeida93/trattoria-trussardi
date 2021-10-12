from typing import List, Optional
from pydantic import BaseModel


class Pratos(BaseModel):
    
    id : Optional[int] = None
    nome : str
    tipo : str
    disponivel : str
    preco : str
    
    class Config:
        orm_mode = True

class Pedidos(BaseModel):
    
    id : Optional[int] = None
    user_id : int
    produto_id : int
    prato_id : int
    
    class Config:
        orm_mode = True
    
class Usuarios(BaseModel):
    
    id : Optional[int] = None
    nome : str
    email : str
    senha : str
    tipo_acesso : str
    
    class Config:
        orm_mode = True
    
    
    