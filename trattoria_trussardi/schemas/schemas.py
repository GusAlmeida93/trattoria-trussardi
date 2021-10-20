from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class Pratos(BaseModel):
    
    id : Optional[int] = None
    nome : str
    tipo : str
    disponivel : bool
    preco : float
    data_criacao : Optional[datetime] = None
    data_atualizacao : Optional[datetime] = None
    
    class Config:
        orm_mode = True

class Usuarios(BaseModel):
    
    id : Optional[int] = None
    nome : str
    email : str
    senha : str
    tipo_acesso : str
    data_criacao : Optional[datetime] = None
    data_atualizacao : Optional[datetime] = None
    class Config:
        orm_mode = True

class UsuariosResponse(BaseModel):
    
    id : Optional[int] = None
    nome : str
    email : str
    tipo_acesso : str
    data_criacao : Optional[datetime] = None
    data_atualizacao : Optional[datetime] = None
    class Config:
        orm_mode = True
        
class Clientes(BaseModel):
    
    id : Optional[int] = None
    nome : str
    email : str
    senha : str
    data_criacao : Optional[datetime] = None
    data_atualizacao : Optional[datetime] = None
    class Config:
        orm_mode = True
        
class ClientesResponse(BaseModel):
    
    id : Optional[int] = None
    nome : str
    email : str
    data_criacao : Optional[datetime] = None
    data_atualizacao : Optional[datetime] = None
    class Config:
        orm_mode = True

class Pedidos(BaseModel):
    
    id : Optional[int] = None
    status : str
    data_criacao : Optional[datetime] = None
    data_atualizacao : Optional[datetime] = None
    cliente_id : int
    cliente : Optional[ClientesResponse]
    prato_id : int
    prato : Optional[Pratos]
    class Config:
        orm_mode = True

    
    
    
    