from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from trattoria_trussardi.database.database import Base


class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    tipo_acesso = Column(String)

class Pedidos(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('usuarios.id'))
    prato_id = Column(Integer, ForeignKey('pratos.id'))

class Pratos(Base):
    __tablename__ = 'pratos'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(String)
    disponivel = Column(Boolean)
    preco = Column(Float)
    
    