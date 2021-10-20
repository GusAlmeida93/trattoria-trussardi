from sqlalchemy.orm import Session
from sqlalchemy import select
from trattoria_trussardi.schemas import schemas
from trattoria_trussardi.models import models

class Clientes:
    
    def __init__(self, session : Session) -> None:
        self.session = session
        
    def criar(self, cliente : schemas.Clientes):
        db_cliente = models.Clientes(nome = cliente.nome,
                                     email = cliente.email,
                                     senha = cliente.senha)
        self.session.add(db_cliente)
        self.session.commit()
        self.session.refresh(db_cliente)
        return db_cliente

    def listar(self):
        
        query = select(models.Clientes)
        clientes = self.session.execute(query).scalars().all()
        return clientes