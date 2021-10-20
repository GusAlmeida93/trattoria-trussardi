import datetime
import pytz
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from trattoria_trussardi.database.database import Base


class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    tipo_acesso = Column(String)
    data_criacao = Column(DateTime, default=datetime.datetime.now(pytz.timezone('America/Sao_Paulo')))
    data_atualizacao = Column(DateTime, default=datetime.datetime.now(pytz.timezone('America/Sao_Paulo')))
    
class Pratos(Base):
    __tablename__ = 'pratos'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(String)
    disponivel = Column(Boolean)
    preco = Column(Float)
    data_criacao = Column(DateTime, default=datetime.datetime.now(pytz.timezone('America/Sao_Paulo')))
    data_atualizacao = Column(DateTime, default=datetime.datetime.now(pytz.timezone('America/Sao_Paulo')))
    
    pedidos = relationship('Pedidos', back_populates='pratos')

    
class Clientes(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    data_criacao = Column(DateTime, default=datetime.datetime.now(pytz.timezone('America/Sao_Paulo')))
    data_atualizacao = Column(DateTime, default=datetime.datetime.now(pytz.timezone('America/Sao_Paulo')))
    
    pedidos = relationship('Pedidos', back_populates='clientes')
    
      
class Pedidos(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True, index=True, unique=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id', name='fk_clientes'))
    prato_id = Column(Integer, ForeignKey('pratos.id', name='fk_pratos'))
    status = Column(String)
    data_criacao = Column(DateTime, default=datetime.datetime.now(pytz.timezone('America/Sao_Paulo')))
    data_atualizacao = Column(DateTime, default=datetime.datetime.now(pytz.timezone('America/Sao_Paulo')))
    
    pratos = relationship('Pratos', back_populates='pedidos')
    clientes = relationship('Clientes', back_populates='pedidos')
    
    

    
    